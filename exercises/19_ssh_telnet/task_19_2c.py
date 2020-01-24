# -*- coding: utf-8 -*-
'''
Задание 19.2c

Скопировать функцию send_config_commands из задания 19.2b и переделать ее таким образом:

Если при выполнении команды возникла ошибка,
спросить пользователя надо ли выполнять остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды. Это значение по умолчанию, поэтому нажатие любой комбинации воспринимается как y
* n или no - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.

Пример работы функции:

In [11]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: y
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: n

In [12]: pprint(result)
({},
 {'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

'''

import netmiko
import yaml
import re
from pprint import pprint

def send_config_commands(device, command, verbose = True):
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    r1= devices[0]
    if verbose:
        print('Подключаюсь к устройству {}'.format(r1['ip']))
    ssh = netmiko.ConnectHandler(**r1)
    ssh.enable()

    result =()
    bad = {}
    good = {}
    for com in command:
        regex = (r'Invalid .* marker.|Incomplete command.|Ambiguous command:\s\s"\w"')
        out = ssh.send_config_set(com)
        match = re.search(regex, out)
        if match:
            err = match.group()
            print('Команда "{}" выполнилась с ошибкой "{}" на устройстве {}'.format(com,err,r1['ip']))
            a = input('Продолжать выполнять команды? [y]/n: ')
            if a == 'y':
                bad[com] = out
                pass
            elif a == 'n' or 'no':
                bad[com] = out
                break
        else:
            good[com] = out
    result=(good, bad)
    print('')
    pprint(result)
    return result

if __name__ == "__main__":

# списки команд с ошибками и без:
    commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
    correct_commands = ['logging buffered 20010', 'ip http server']

    commands = commands_with_errors + correct_commands
    send_config_commands('devices.yaml', commands)
    #send_config_commands('devices.yaml', commands, verbose=False)
