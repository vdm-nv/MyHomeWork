# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к одному устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_show_command.

'''
import netmiko
from pprint import pprint
import yaml


def send_show_command(device,command):
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    #for dev in devices:
    '''
ConnectHandler устанавливается соединение с устройством на основе параметров, которые находятся в словаре.
две звездочки перед словарем - это распаковка словаря
    '''
    ssh = netmiko.ConnectHandler(**devices[0])
    ssh.enable()
    out = ssh.send_command(command)
    pprint(out)
    return out

if __name__ == "__main__":
    command = 'sh ip int br'
    send_show_command('devices.yaml',command)
