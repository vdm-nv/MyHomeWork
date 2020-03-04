# -*- coding: utf-8 -*-
'''
Задание 22.1

Создать функцию parse_command_output. Параметры функции:
* template - шаблон TextFSM. Имя файла, в котором находится шаблон
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список:
* первый элемент - это список с названиями столбцов
* остальные элементы это списки, в котором находятся результаты обработки вывода

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.

'''
import sys
import textfsm
from tabulate import tabulate
from pprint import pprint


def parse_command_output(template, output_file):

    with open(template) as f:
        re_table = textfsm.TextFSM(f)
        header = re_table.header
        result = re_table.ParseText(output_file)
#        print(result)
#        print(tabulate(result, headers=header))
    result.insert(0, header)
    return result

if __name__ == "__main__":
    with open("output/sh_ip_int_br.txt") as f:
        out = f.read()
    pprint(parse_command_output('templates/sh_ip_int_br.template', out))
