# -*- coding: utf-8 -*-
'''
Задание 22.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами. Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - templates

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
'''
import sys
import clitable
from pprint import pprint

def parse_command_dynamic(command_output,attributes_dict):

    cli = clitable.CliTable('index', 'templates') # что бы работал pytest use "index", что бы скрипт работал самостоятельно "use index_file"
    cli.ParseCmd(command_output, attributes_dict)

    data_rows = [list(row) for row in cli]      # добавляем row from cli to list
    header = list(cli.header)                   # add to headers to list
    data = []

    for d in data_rows:
        data.append(dict(zip(header,d)))        # долаем список словарей
    return data

if __name__ == "__main__":
    output = open('output/sh_ip_int_br.txt').read()
    attributes = {'Command': 'sh ip int br' , 'Vendor': 'Cisco'}
    pprint(parse_command_dynamic(output, attributes))
