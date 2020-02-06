# -*- coding: utf-8 -*-
'''
Задание 20.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.
'''
from concurrent.futures import ThreadPoolExecutor, as_completed
import subprocess

result = ()
reachable = []
unreachable = []

def ping_ip_addresses(ip_list, limit=3):
    for ip in ip_list:
        print(f'PINGING {ip}')
        res = subprocess.run('ping {} -c 2 -n'.format(ip),
                             shell=True,stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, encoding='utf-8')
        if res.returncode == 0:
            reachable.append(ip)
        else:
            unreachable.append(ip)

    result=(reachable,unreachable)
    return result

test = ['1.1.1', '8.8.8.8', '8.8.4.4', '8.8.7.1']

print(ping_ip_addresses(test))
