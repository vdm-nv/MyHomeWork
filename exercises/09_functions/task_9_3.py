# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
result = ()
access = {}
trunk = {}

def get_int_vlan_map(config_filename):
    with open(config_filename) as f:
        for line in f:
            if 'FastEth' in line:           # ищем fasteth
                intf_a = line.split()[1]
            elif 'access vlan' in line:     # и если есть acces vl
                vl_a = line.split()[-1]
                access[intf_a] = int(vl_a)       # добавляем значение access intf и vlan в числовом значении
            if 'FastEth' in line:
                intf_b = line.split()[1]
            elif 'allowed vlan' in line:
                vl_b = line.split()
                vlvl = []
                vl = vl_b[-1].split(',')
                for i in vl:
                    vlvl.append(int(i))
                trunk[intf_b] = vlvl
                result = (access, trunk)

        return result
