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
    result = []
    for line in fread:
        if line.count('.') == 2:
            p = line.replace('DYNAMIC', '')
            result.append(p.split()) # make list in list
    k = []
    big = []
    for lists in result:
        for item in lists:
            if item.isdigit():
                k.append(int(item))   # make integer in  item[0]
            else:
                k.append(item)
        # make again list in list
        big = [k[x:x+3] for x in range(0, len(k) - 2, 3)]
        big.sort()
#    print('\n'.join(str(x) for x in big))

x = int(input('Enter Vlan: '))

for item in big:
    if x in item:
        print('  '.join(str(x) for x in item))

