#!/usr/bin/env python3

'''
Задание 6.2a
'''
add = input('Введите IP адрес: ')

bb = add.split('.')
          
octets = []
broad = ['255','255','255','255']
unass = ['0', '0', '0', '0']

for did in bb:
  if did.isdigit() != True:
    print('\n'+ '-'*30)
    print('Please input only digits')
    break
    print('-'*30)

for addr in bb:
    octets.append((addr))
    
while True:
  if add.count('.') != 3:
    print('\n'+ '-'*30)
    print('please input digits by dots')
    break
    print('-'*30)
  elif int(bb[0]) > 0 and int(bb[0]) <= 223:
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
