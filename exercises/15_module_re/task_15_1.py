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
from pprint import pprint

def get_ip_from_cfg(filename):             # регулярные выражения обьявлены в переменную
    regex =(' ip address (\S+) (\S+)')

    result = []

    with open(filename) as f:
        for line in f:
            match = re.search(regex, line)
            if match:
                ip = match.group(1)
                mask = match.group(2)
                result.append((ip,mask))
    return result

def get_ip_from_cfg_01(filename):           # регулярные выражения в середине цикла фукции
    result = []

    with open(filename) as f:
        for line in f:
            if line.startswith(' ip address'):
                match = re.search(r' .* (\S+) (\S+)',line)
                ip = match.group(1)
                mask = match.group(2)
                result.append((ip,mask))
    return result

if __name__ == "__main__":
    result = get_ip_from_cfg('config_r1.txt')   #использует функцию get_ip_from_cfg
    pprint(result)

