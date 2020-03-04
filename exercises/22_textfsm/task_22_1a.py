# -*- coding: utf-8 -*-
'''
Задание 22.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - шаблон TextFSM. Имя файла, в котором находится шаблон
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt и шаблоне templates/sh_ip_int_br.template.
'''
import sys
import textfsm
from pprint import pprint


def parse_output_to_dict(template, output_file):

    with open(template) as f:
        re_table = textfsm.TextFSM(f)
        header = re_table.header
        result = re_table.ParseText(output_file)
#        print(result)
#        print(tabulate(result, headers=header))

    data = []
    for item in result:
        data.append(dict(zip(header, item)))

    return data

if __name__ == "__main__":
    with open("output/sh_ip_int_br.txt") as f:
        out = f.read()
    pprint(parse_output_to_dict('templates/sh_ip_int_br.template', out))
