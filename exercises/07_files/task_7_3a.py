#!/usr/bin/env python3

'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:

10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9
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
    for item in big:
        print('{:<8}{:<12}{:>8}'.format(*item))
