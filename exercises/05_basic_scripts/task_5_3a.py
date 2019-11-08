#!/usr/bin/env python3


#Задание 5.3a

'''
Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
    * для access: 'Введите номер VLAN:'
    * для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.

То есть эту задачу можно решить без использования условия if и циклов for/while.
'''


access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
            ]
trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

sw = {
    'access':
    {
        'switchport mode access': '',
        'switchport access vlan {}' : '',
        'switchport nonegotiate' : '',
        'spanning-tree portfast' : '',
        'spanning-tree bpduguard enable' : ''
    },
    'trunk': {
        'switchport trunk encapsulation dot1q': '',
        'switchport mode trunk': '',
        'switchport trunk allowed vlan {}': ''}
}

vlans = {
    'access':{
        'Введите номер VLAN:': ''},
    'trunk': {
        'Введите разрешенные VLANs:' : '' }
}


mode_intf = input('Введите режим работы интерфейса (access/trunk):')

d_keys = sw[mode_intf].keys()
v_keys = vlans[mode_intf].keys()

type_intf = input('Введите тип и номер интерфейса:')
vl = input(list(v_keys))

print('\n' + '-' * 30)
print('\n' + 'interface {}'.format(type_intf))
print('\n'.join(d_keys).format(vl))
print('\n' + '-' * 30 + '\n')

