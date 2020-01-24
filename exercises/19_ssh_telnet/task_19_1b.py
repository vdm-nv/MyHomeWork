# -*- coding: utf-8 -*-
'''
Задание 19.1b

Скопировать функцию send_show_command из задания 19.1a и переделать ее таким образом,
чтобы обрабатывалось не только исключение, которое генерируется
при ошибке аутентификации на устройстве, но и исключение,
которое генерируется, когда IP-адрес устройства недоступен.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
'''
import netmiko
from pprint import pprint
import yaml


def send_show_command(device,command):
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    try:
        ssh = netmiko.ConnectHandler(**devices[0])
    except netmiko.NetMikoTimeoutException as err_timeout:
        print(err_timeout)
    except netmiko.NetMikoAuthenticationException as err:
        print(err)

if __name__ == "__main__":
    command = 'sh ip int br'
    send_show_command('devices.yaml',command)

