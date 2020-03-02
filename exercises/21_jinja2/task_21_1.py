# -*- coding: utf-8 -*-
'''
Задание 21.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных из файла data_files/for.yml.

'''
from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os

dir_d = os.path.abspath('data_files')

def generate_config(temp, d):
    with open(d) as f:
        vars_d = yaml.safe_load(f)

    env = Environment(
            loader=FileSystemLoader('templates'),
            trim_blocks=True,
            lstrip_blocks=True)
    template = env.get_template(temp)
    res = template.render(vars_d)

    return res

if __name__ == '__main__':
    print(generate_config('for.txt','data_files/for.yml'))
