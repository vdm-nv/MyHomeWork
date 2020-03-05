# -*- coding: utf-8 -*-
'''
Задание 22.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show с помощью netmiko,
а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки вывода команды (как в задании 22.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br и устройствах из devices.yaml.
'''
import yaml,netmiko
from pprint import pprint
import clitable

def send_and_parse_show_command(device_dict, command, templates_path):
    print(f"Connecting to {device_dict['ip']}")
    ssh = netmiko.ConnectHandler(**device_dict)
    ssh.enable()
    print(f"Send commamd - \'{command}\' to {device_dict['ip']}\n")
    output = ssh.send_command(command)
    print(f"Got data from {device_dict['ip']}\n")

    cli = clitable.CliTable('index_file', templates_path)
    attributes = {'Command': 'sh ip int br' , 'Vendor': 'Cisco'}
    cli.ParseCmd(output, attributes)
    data_rows = [list(row) for row in cli]
    
    data = []
    for d in data_rows:
        data.append(dict(zip(list(cli.header), d)))
    print("Parsing result you can see below:")
    return data

if __name__ == "__main__":
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    r1 = devices[0]
    pprint(send_and_parse_show_command(r1,'sh ip int br', 'templates'))
