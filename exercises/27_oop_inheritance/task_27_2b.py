# -*- coding: utf-8 -*-

'''
Задание 27.2b

Дополнить класс MyNetmiko из задания 27.2a.

Переписать метод send_config_set netmiko, добавив в него проверку на ошибки с помощью метода _check_error_in_command.

Метод send_config_set должен отправлять команды по одной и проверять каждую на ошибки.
Если при выполнении команд не обнаружены ошибки, метод send_config_set возвращает вывод команд.

In [2]: from task_27_2b import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_config_set('lo')
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-2-8e491f78b235> in <module>()
----> 1 r1.send_config_set('lo')

...
ErrorInCommand: При выполнении команды "lo" на устройстве 192.168.100.1 возникла ошибка "Incomplete command."

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

    def send_command(self, command):
        result = super().send_command(command)
        self._check_error_in_command(command, result)
        return result

    def send_config_set(self, command):
        result = super().send_config_set(command)
        self._check_error_in_command(command, result)
        return result
