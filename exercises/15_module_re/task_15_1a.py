# -*- coding: utf-8 -*-
'''
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re

def get_ip_from_cfg(filename):

    res = {}

    with open(filename) as f:
        for line in f:
            if 'interface ' in line:
                k = re.search('interface (\S+)', line).group(1)

            elif line.startswith(' ip address'):
                ip = re.search('^ ip address (\S+) (\S+)',line).group(1)
                mask = re.search('^ ip address (\S+) (\S+)',line).group(2)
                res[k] = (ip,mask)
    return res
#print(get_ip_from_cfg('config_r1.txt'))
