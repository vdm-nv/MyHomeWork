# -*- coding: utf-8 -*-

'''
Задание 27.1a

Дополнить класс CiscoSSH из задания 27.1.

Перед подключением по SSH необходимо проверить если ли в словаре
с параметрами подключения такие параметры: username, password, secret.
Если нет, запросить их у пользователя, а затем выполнять подключение.

In [1]: from task_27_1a import CiscoSSH

In [2]: device_params = {
   ...:         'device_type': 'cisco_ios',
   ...:         'ip': '192.168.100.1',
   ...: }

In [3]: r1 = CiscoSSH(**device_params)
Введите имя пользователя: cisco
Введите пароль:
Введите пароль для режима enable:

In [4]: r1.send_show_command('sh ip int br')
Out[4]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

'''
import getpass
from base_connect_class import BaseSSH
from pprint import pprint
device_params = {
    'device_type': 'cisco_ios',
    'ip': '192.168.100.1'
}

class CiscoSSH(BaseSSH):
    def __init__(self, **device_params):
        keys_params = ['username', 'password', 'secret']
        for word in keys_params:
            if word == 'username' and word not in device_params:
                a = input('Введите им пользователя: ')
                device_params['username'] = a
                #print(device_params)
            elif word == 'password' and word not in device_params:
                a = getpass.getpass('Введите пароль: ')
                device_params['password'] = a
            elif word == 'secret' and word not in device_params:
                a = getpass.getpass('Введите пароль для режима enable: ')
                device_params['secret'] = a
                pprint(device_params)
        super().__init__(**device_params)
        self.ssh.enable()

if __name__ == '__main__':
    r1 = CiscoSSH(**device_params)
    print(r1.send_show_command('sh ip int br'))

