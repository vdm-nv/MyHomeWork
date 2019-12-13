# -*- coding: utf-8 -*-
'''
Задание 15.1

Создать функцию get_ip_from_cfg, которая ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски,
которые настроены на интерфейсах, в виде списка кортежей:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например (взяты произвольные адреса):
[('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.


Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re

def get_ip_from_cfg(filename):

    res = []

    with open(filename) as f:
        for line in f:
            if line.startswith(' ip address'):
                match = re.search(r' .* (\S+) (\S+)',line)
                ip = match.group(1)
                mask = match.group(2)
                res.append((ip,mask))

        return res

print(get_ip_from_cfg('config_r1.txt'))

####Version_02
#regex =(' ip address (\S+) (\S+)')
#
#res = []
#with open('config_r1.txt') as f:
#     for line in f:
#         match = re.search(regex, line)
#         if match:
#             ip = match.group(1)
#             mask = match.group(2)
#             res.append((ip,mask))
#     print(res)
