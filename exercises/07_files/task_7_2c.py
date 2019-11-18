#!/usr/bin/env python3

'''
Задание 7.2c

Переделать скрипт из задания 7.2b:

* передавать как аргументы скрипту:
* имя исходного файла конфигурации
* имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

file_name = argv[1]
new_file_name =argv[2]

with open(file_name) as scr, open(new_file_name, 'w') as dest:
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
            dest.writelines(line+'\n')
            print(line)
