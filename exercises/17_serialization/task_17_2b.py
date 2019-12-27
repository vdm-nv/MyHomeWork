<<<<<<< HEAD
# -*- coding: utf-8 -*-
'''
Задание 17.2b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует draw_topology).

Проверить работу функции на файле topology.yaml. На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology.

Результат должен выглядеть так же, как схема в файле task_17_2b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
import re
import yaml
import glob
from draw_network_graph import draw_topology

files = glob.glob('sh_cdp_n*')

d={}
regex = (r'(\S+)>.+')
regex01 = (r'(\S+) + (\w{3} \d\/\d) .+ (\w{3} \d\/\d)')

=======
'''
>>>>>>> 7840f404a2b4e197c2a041f41582c65408360363
for item in files:
    with open(item) as f:
        for line in f:
            m = re.search(regex,line)
            if m:
                loc_d = m.group(1)
            m01 = re.search(regex01,line)
            if m01:
                rem_d,loc_p,rem_p = m01.groups()
                v=(rem_d,rem_p)
                if v not in d:
                    d[loc_d,loc_p]=v
<<<<<<< HEAD

    with open('topology.yaml','w') as f:
            temp = yaml.dump(d,f)

def transform_topology(file):
    with open(file) as f:
        temp = yaml.load(f)
    return temp

draw_topology(transform_topology('topology.yaml'))

=======
with open('topology.yaml','w') as f:
    temp = yaml.dump(d,f)
    '''
>>>>>>> 7840f404a2b4e197c2a041f41582c65408360363
