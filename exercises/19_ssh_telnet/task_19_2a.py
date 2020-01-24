# -*- coding: utf-8 -*-
'''
Задание 19.2a

Скопировать функцию send_config_commands из задания 19.2 и добавить параметр verbose,
который контролирует будет ли выводится на стандартный поток вывода
информация о том к какому устройству выполняется подключение.

verbose - это параметр функции send_config_commands, не параметр ConnectHandler!

По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, verbose=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства из файла devices.yaml с помощью функции send_config_commands.
'''
import netmiko
import yaml
from pprint import pprint

def send_config_commands(device, command, verbose = True):
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
        r1= devices[0]
    if verbose:
        print('Подключаюсь к устройству {}'.format(r1['ip']))
    ssh = netmiko.ConnectHandler(**r1)
    ssh.enable()
    out = ssh.send_config_set(command)
    return out

if __name__ == "__main__":
    commands = ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']
    send_config_commands('devices.yaml', commands)
    send_config_commands('devices.yaml', commands, verbose=False)
