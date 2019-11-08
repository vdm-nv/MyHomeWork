#!/usr/bin/env python3

#Задание 5.2b
#
#Преобразовать скрипт из задания 5.2a таким образом,
#чтобы сеть/маска не запрашивались у пользователя,
#а передавались как аргумент скрипту.
#
#Ограничение: Все задания надо выполнять используя только пройденные темы.

from sys import argv

#netw = input('Введите адрес IP-сети:')
#mask = input('Введите маску сети:')

netw = argv[1]
mask = argv[2]
#
# or netw,mask = argv[1:3]

add = netw.split('.')
mas = mask.split()

ip_temp = '''
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

print('\n' + '-' * 30)
print('\n' + 'Network:' + ip_temp.format(int(add[0]),int(add[1]),int(add[2]),int(0)))
print('\n' + 'Mask:'+ '\n'+ mask)# + ip_temp.format(int(add[0]),int(add[1]),int(add[2]),int(add[3])))
print('\n' + '-' * 30)

