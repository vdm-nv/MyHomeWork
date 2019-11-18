#!/usr/bin/env python3

'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
    - Запросить у пользователя ввод номера VLAN.
    - Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''


with open('CAM_table.txt') as f:
    fread = f.readlines()
    x = input('Enter Vlan: ')
    for line in fread:
        if x in line:
            print(line.replace('DYNAMIC',''))
