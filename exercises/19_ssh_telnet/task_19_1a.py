# -*- coding: utf-8 -*-
'''
Задание 19.1a

Скопировать функцию send_show_command из задания 19.1 и переделать ее таким образом,
чтобы обрабатывалось исключение, которое генерируется
при ошибке аутентификации на устройстве.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
'''
import netmiko
from pprint import pprint
import yaml


def send_show_command(device,command):
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    try:
        ssh = netmiko.ConnectHandler(**devices[0])
    except netmiko.NetMikoAuthenticationException as err:
        print(err)
#    ssh.enable()
#       out = ssh.send_command(command)
#       pprint(out)
#       return out

if __name__ == "__main__":
    command = 'sh ip int br'
    send_show_command('devices.yaml',command)
