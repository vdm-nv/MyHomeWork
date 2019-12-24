'''
Задание 11.2
Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.
У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.
Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}
Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
В словаре, который возвращает функция create_network_map, не должно быть дублей.
С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg
При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
Не копировать код функций parse_cdp_neighbors и draw_topology.
Ограничение: Все задания надо выполнять используя только пройденные темы.
> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz
> И модуль python для работы с graphviz:
> pip install graphviz
'''
#!/usr/bin/env python3
from draw_network_graph import draw_topology

ff = ['sh_cdp_n_sw1.txt','sh_cdp_n_r1.txt','sh_cdp_n_r2.txt','sh_cdp_n_r3.txt']

def create_network_map(filenames):
    
    res = {}
    output_from_files = []
    
    for item in ff:
        with open(item) as f:
            sh = f.read().rstrip()
            output_from_files.append(sh.lstrip().split('\n'))

    for item in output_from_files:
        for i in item:
            if i.startswith('SW1>'):
                k = [i[0:3]]
            elif i.startswith('R1>'):
                k = [i[0:2]]
            elif i.startswith('R2>'):
                k = [i[0:2]]
            elif i.startswith('R3>'):
                k = [i[0:2]]
            elif 'Eth' in i:
                rem_dev,local_i,local_p,*rest,rem_i,rem_p = i.split()
                k.append(local_i+local_p)
                v = (rem_dev, rem_i + rem_p)
                if v not in res:                    #если нет значения в словаре, тогда добавляем вывод в словарь
                    res[tuple(k)]= (v)
                k.pop(-1)
    return res

draw_topology(res)
