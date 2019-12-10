# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import subprocess

res = ()
reach = []
unreach = []

def ping_ip_addresses(ip_address):
    for ip in ip_address:
        print('Now we are try to reach', ip)
        result = subprocess.run('ping {} -c 2 -n'.format(ip),
                                shell=True,stdout=subprocess.PIPE,          #stdout=subprocess.PIPE - запись вывода стандартного поток 
                                stderr=subprocess.PIPE, encoding='utf-8')   #stderr=subprocess.PIPE Работа со стандартным потоком ошибок
        if result.returncode == 0: # Код 0 означает, что программа выполнилась успешно.
            reach.append(ip)
            #print('\n its working IP', reach)
        else:
            unreach.append(ip)
            #print('\n IP is unreachable', unreach)
    res = (reach,unreach)
    return res
#Out[48]: (['8.8.8.8', '8.8.4.4'], ['1.1.1', '8.8.7.1'])

