# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
'''
import re
from pprint import pprint

def get_ints_without_description(filename):
    d = {}
    res = []
    with open(filename) as f:
        for line in f:
            if line.startswith('interface'):
                d_keys = re.search('interface (\S+)', line).group(1)
                d[d_keys]= None
            elif line.startswith(' description'):
                d_values = line.rstrip()
                d[d_keys]= d_values

    for k,v in d.items():
        if v == None:
            res.append(k)
    return res
pprint(get_ints_without_description('config_r1.txt'))
