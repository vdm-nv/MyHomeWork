# -*- coding: utf-8 -*-
'''
Задание 17.2a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод команды show cdp neighbor из нескольких файлов и записывает итоговую топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами, независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь в файл topology.yaml.

'''
import re 
import yaml
import glob

files = glob.glob('sh_cdp_n*')

def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    d= {}
    regex = (r'(\S+)>.+')
    regex01 = (r'(\S+) + (\w{3} \d\/\d) .+ (\w{3} \d\/\d)')

    for item in list_of_files:
        with open(item) as f:
            for line in f:
                m = re.search(regex,line)               # отбираем R1> или SW1>
                if m:
                    gl_k= m.group(1)
                    d[gl_k]={}
                m01 = re.search(regex01,line)           # отбираем (SW1, Eth 0/0, Eth 0/1)
                if m01:
                    rem_d = m01.group(1)
                    loc_p = m01.group(2)
                    rem_p = m01.group(3)
                    d[gl_k][loc_p]={rem_d: rem_p}

    if save_to_filename is None:
        pass
    else:
        with open(save_to_filename, 'w') as f:
            yaml.dump(d,f)
    return d
print(generate_topology_from_cdp(files))
