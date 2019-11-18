#!/usr/bin/env python3

'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:

    * вместо вывода на стандартный поток вывода,
    скрипт должен записать полученные строки в файл config_sw1_cleared.txt
    При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.


Строки, которые начинаются на '!' отфильтровывать не нужно.
Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

file_name = argv[1]

with open(file_name) as scr, open('config_sw1_cleared.txt', 'w') as dest:
    for line in scr:
        line = line.rstrip()

        # Если начинается на '!'
#        if line == '!':
#            continue

        # Если пустая строка
        if not line:
            continue

        #if 'Current' not in line and 'duplex' not in line and 'alias' not in line:
        #     print(line)
        if not any(word in line for word in ignore):
            dest.write(line)
