#!/usr/bin/env python3

#Переделать скрипт из задания 5.1a таким образом, чтобы, при запросе параметра,
#отображался список возможных параметров. Список параметров надо получить из словаря,
#а не прописывать вручную.
#Вывести информацию о соответствующем параметре, указанного устройства.
#Пример выполнения скрипта:
#    $ python task_5_1b.py
#    Введите имя устройства: r1
#    Введите имя параметра (ios, model, vendor, location, ip): ip
#    10.255.0.1


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
param = input('Введите необходимый параметр.{}:'.format(london_keys))

print('\n' + '-' * 30)
print('\n' + london_co[name][param])
print('\n' + '-' * 30 + '\n')
