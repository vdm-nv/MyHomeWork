#!/usr/bin/env python3

# Задание 5.1d
# Переделать скрипт из задания 5.1c таким образом, чтобы, при запросе параметра,
# пользователь мог вводить название параметра в любом регистре.
# Пример выполнения скрипта:
#    $ python task_5_1d.py
#    Введите имя устройства: r1
#    Введите имя параметра (ios, model, vendor, location, ip): IOS
#    15.4

london_co = {
        'r1': {
                    'location': '21 New Globe Walk',
                    'vendor': 'Cisco',
                    'model': '4451',
                    'ios': '15.4',
                    'ip': '10.255.0.1'
                },
        'r2': {
                    'location': '21 New Globe Walk',
                    'vendor': 'Cisco',
                    'model': '4451',
                    'ios': '15.4',
                    'ip': '10.255.0.2'
                },
        'sw1': {
                    'location': '21 New Globe Walk',
                    'vendor': 'Cisco',
                    'model': '3850',
                    'ios': '3.6.XE',
                    'ip': '10.255.0.101',
                    'vlans': '10,20,30',
                    'routing': True
                }
}


name = input('Введите имя устройства:')
london_keys = tuple(london_co[name].keys())
param = str.lower(input('Введите необходимый параметр. {}:'.format(london_keys)))

print('\n' + '-' * 30)
print('\n'+ london_co[name].get( param, 'Такого параметра нет' ))
print('\n' + '-' * 30 + '\n')
