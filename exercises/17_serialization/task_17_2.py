# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''
import re

with open('sh_cdp_n_sw1.txt') as f:
    sh_cdp = f.read()

def parse_sh_cdp_neighbors(sh_cdp):

    regex = (r'\s(\S+\d)>.+\s{2}.+\s.+\s{2}.+\s'
             r'(\w\d) +(\w{3} \d\/\d) .+ (\w{3} \d\/\d)\s'
             r'(\w\d) +(\w{3} \d\/\d) .+ (\w{3} \d\/\d)\s'
             r'(\w\d) +(\w{3} \d\/\d) .+ (\w{3} \d\/\d)\s'
             r'(\w\d) +(\w{3} \d\/\d) .+ (\w{3} \d\/\d)\s')

    res = re.search(regex, sh_cdp)
    l = list(res.groups())
    l.pop(0)
    res1 = [l[d:d+3] for d in range(0, len(l),3)]
    k = 'SW1'
    d = {}
    d[k] = {}
    for item in res1:
        rem_d,local_p,rem_p = item
        d[k][local_p]={rem_d:rem_p}
    return d
print(parse_sh_cdp_neighbors(sh_cdp))



