# -*- coding: utf-8 -*-
'''
Задание 15.2a

Создать функцию convert_to_dict, которая ожидает два аргумента:
* список с названиями полей
* список кортежей со значениями

Функция возвращает результат в виде списка словарей, где ключи - взяты из первого списка,
а значения подставлены из второго.

Например, если функции передать как аргументы список headers и список
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 'FastEthernet0/1', '10.0.2.1', 'up', 'up')]

Функция должна вернуть такой список со словарями (порядок полей может быть другой):
[{'interface': 'FastEthernet0/0', 'address': '10.0.1.1', 'status': 'up', 'protocol': 'up'},
 {'interface': 'FastEthernet0/1', 'address': '10.0.2.1', 'status': 'up', 'protocol': 'up'}]

Проверить работу функции:
* первый аргумент - список headers
* второй аргумент - результат, который возвращает функция parse_sh_ip_int_br из задания 15.2, если ей как аргумент передать sh_ip_int_br.txt.

Функцию parse_sh_ip_int_br не нужно копировать.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import re
from task_15_2 import parse_sh_ip_int_br

headers = ['interface', 'address', 'status', 'protocol']

result = []

int_br = parse_sh_ip_int_br('sh_ip_int_br.txt')

def convert_to_dict(heads,int_br):

    for item in int_br:
        result.append(dict(zip(heads,item)))
    return result
print(result)


