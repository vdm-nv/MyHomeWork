#!/usr/bin/env python3

'''
Задание 6.2a
'''
   


add = input('Введите IP адрес: ')

bb = add.split('.')

if add.count('.') != 3:
    print('please input digits by dots')
    for did in bb:
        if did.isdigit() != True:
            print('Please input only digits')
            
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
