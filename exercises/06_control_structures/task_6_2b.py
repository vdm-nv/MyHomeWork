#!/usr/bin/env python3

'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.
Дополнить скрипт:

Если адрес был введен неправильно, запросить адрес снова.
'''

add = input('Введите IP адрес: ')

bb = add.split('.')
          
octets = []
broad = ['255','255','255','255']
unass = ['0', '0', '0', '0']

for dig in bb:
  if dig.isdigit() != True or add.count('.') != 3:
    print('\n' + '-'*30)
    print('Please input only digits')
    print('\n' + '-'*30)
    add = input('Введите IP адрес ещё раз!: ')
    bb = add.split('.')
    break
    

for addr in bb:
    if int(addr) >= 0 and int(addr) <= 255:
          octets.append((addr))
    else:
      print('Please input only digit in octet from 0 to 255')
      add = input('Введите IP адрес: ')
      break
  
octets = []
bb = add.split('.')

for addr in bb:
    if int(addr) >= 0 and int(addr) <= 255:
          octets.append((addr))

while True:
    if int(bb[0]) > 0 and int(bb[0]) <= 223:
      print('\n'+ '-'*30)
      print('Это unicast')
      print('-'*30)
    elif int(bb[0]) >= 224 and int(bb[0])<= 239:
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
    break
