#!/usr/bin/env python3

'''
Задание 6.2
1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
       'unicast' - если первый байт в диапазоне 1-223
       'multicast' - если первый байт в диапазоне 224-239
       'local broadcast' - если IP-адрес равен 255.255.255.255
       'unassigned' - если IP-адрес равен 0.0.0.0
       'unused' - во всех остальных случаях
Ограничение: Все задания надо выполнять используя только пройденные темы.
                   '''

add = input('Введите IP адрес: ')

bb = add.split('.')

octets = []

broad = [255, 255, 255, 255]

unass = [0, 0, 0, 0]



for addr in bb:
    octets.append(int(addr))


if int(bb[0]) <= 223:
    print('\n'+ '-'*30)
    print('Это unicast')
    print('-'*30)
elif int(bb[0]) <= 239:
    print('\n'+ '-'*30)
    print('Это multicast')
    print('\n'+ '-'*30)
elif octets == broad:
    print('\n'+ '-'*30)
    print('Это local broadcast')
    print('-'*30)
elif octets == unass:
    print('\n'+ '-'*30)
    print('Это unassagnet')
    print('-'*30)
else:
    print('\n'+ '-'*30)
    print('Это unused')
    print('-'*30)

