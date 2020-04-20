# -*- coding: utf-8 -*-

'''
Задание 27.2c

Проверить, что метод send_command класса MyNetmiko из задания 27.2b, принимает дополнительные аргументы (как в netmiko), кроме команды.

Если возникает ошибка, переделать метод таким образом, чтобы он принимал любые аргументы, которые поддерживает netmiko.


In [2]: from task_27_2c import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_command('sh ip int br', strip_command=False)
Out[4]: 'sh ip int br\nInterface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

In [5]: r1.send_command('sh ip int br', strip_command=True)
Out[5]: 'Interface                  IP-Address      OK? Method Status                Protocol\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \nEthernet0/3                192.168.230.1   YES NVRAM  up                    up      \nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      '

'''
from netmiko.cisco.cisco_ios import CiscoIosBase

class ErrorInCommand(Exception):
        pass


class MyNetmiko(CiscoIosBase):
    def __init__(self, **device_params):
        self.ip = device_params['ip']
        super().__init__(**device_params)
        self.enable()

    def _check_error_in_command(self, command, output_from_device):
        errors = ['Invalid input detected', 'Incomplete command', 'Ambiguous command']
        for error in errors:
            if errors[0] in output_from_device:
                raise ErrorInCommand(f'При выполнении команды \"{command}\" на устройстве {self.ip} возникла ошибка \"{errors[0]}\"')
            elif errors[1] in output_from_device:
                raise ErrorInCommand(f'При выполнении команды \"{command}\" на устройстве {self.ip} возникла ошибка \"{errors[1]}\"')
            elif errors[1] in output_from_device:
                raise ErrorInCommand(f'При выполнении команды \"{command}\" на устройстве {self.ip} возникла ошибка \"{errors[2]}\"')

    def send_command(self, command, **kwargs):
        result = super().send_command(command, **kwargs)
        self._check_error_in_command(command, result)
        return result

    def send_config_set(self, command):
        result = super().send_config_set(command)
        self._check_error_in_command(command, result)
        return result

