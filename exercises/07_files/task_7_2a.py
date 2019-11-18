#!/usr/bin/env python3

'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
Скрипт не должен выводить команды, в которых содержатся слова,
которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

file_name = argv[1]

with open(file_name) as scr:
    for line in scr:
        line = line.rstrip()

        # Если начинается на '!'
        if line == '!':
            continue

        # Если пустая строка
        if not line:
            continue

        #if 'Current' not in line and 'duplex' not in line and 'alias' not in line:
        #     print(line)
        if not any(word in line for word in ignore):
            print(line)
