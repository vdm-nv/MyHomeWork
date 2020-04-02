# -*- coding: utf-8 -*-

'''
Скопировать класс CiscoTelnet из задания 25.2b и изменить метод send_config_commands добавив проверку команд на ошибки.

У метода send_config_commands должен быть дополнительный параметр strict:

strict=True значит, что при обнаружении ошибки, необходимо сгенерировать исключение ValueError
strict=False значит, что при обнаружении ошибки, надо только вывести на стандартный поток вывода сообщене об ошибке
Метод дожен возвращать вывод аналогичный методу send_config_set у netmiko (пример вывода ниже). Текст исключения и ошибки в примере ниже.

Пример создания экземпляра класса:
In [1]: from task_25_2c import CiscoTelnet

In [2]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

In [4]: commands_with_errors = ['logging 0255.255.1', 'logging', 'i']
In [5]: correct_commands = ['logging buffered 20010', 'ip http server']
In [6]: commands = commands_with_errors+correct_commands

Использование метода send_config_commands:
In [7]: print(r1.send_config_commands(commands, strict=False))
При выполнении команды "logging 0255.255.1" на устройстве 192.168.100.1 возникла ошибка -> Invalid input detected at '^' marker.
При выполнении команды "logging" на устройстве 192.168.100.1 возникла ошибка -> Incomplete command.
При выполнении команды "i" на устройстве 192.168.100.1 возникла ошибка -> Ambiguous command:  "i"
conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#logging 0255.255.1
                   ^
% Invalid input detected at '^' marker.

R1(config)#logging
% Incomplete command.

R1(config)#i
% Ambiguous command:  "i"
R1(config)#logging buffered 20010
R1(config)#ip http server
R1(config)#end
R1#

In [8]: print(r1.send_config_commands(commands, strict=True))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-8-0abc1ed8602e> in <module>
----> 1 print(r1.send_config_commands(commands, strict=True))

...

ValueError: При выполнении команды "logging 0255.255.1" на устройстве 192.168.100.1 возникла ошибка -> Invalid input detected at '^' marker.

'''
import textfsm,clitable
import telnetlib
import time,os
from pprint import pprint
import time,re,os
import telnetlib
import textfsm,clitable

class CiscoTelnet:
    def __init__(self, **param):
        self.ip = param['ip']
        self = self._write_line(param)

    def _write_line(self, param):
        self.telnet = telnetlib.Telnet(self.ip)
        self.telnet.read_until(b'Username:')
        self.telnet.write(param['username'].encode('ascii') + b'\n')

        self.telnet.read_until(b'Password:')
        self.telnet.write(param['password'].encode('ascii') + b'\n')
        self.telnet.write(b'enable\n')

        self.telnet.read_until(b'Password:')
        self.telnet.write(param['secret'].encode('ascii') + b'\n')
        self.telnet.write(b'terminal length 0\n')

        time.sleep(0.5)
        self.telnet.read_very_eager()

    def send_show_command(self, command, parse=None, templates=None):
        templates = os.path.join(os.getcwd(), 'templates')
        self.telnet.write(command.encode('ascii') + b'\n')
        time.sleep(1)
        output = self.telnet.read_very_eager().decode('ascii')

        if parse:
            attributes = {'Command': command, 'Vendor': 'cisco_ios'}
            cli_table = clitable.CliTable('index', templates)
            cli_table.ParseCmd(output, attributes)
            data_rows = [list(row) for row in cli_table]
            res = []
            for d in data_rows:
                res.append(dict(zip(list(cli_table.header),d)))
            return res
        else:
            return output
    def send_config_commands(self, commands, strict=None):
        if type(commands) == str:
            commands = [commands]
        out_correct = ''
        self.telnet.write(b'conf t\n')
        for command in commands:
            self.telnet.write(command.encode('ascii') + b'\n')
            time.sleep(0.5)
            out = self.telnet.read_very_eager().decode('ascii')
            regex = (r'Invalid .* marker.|Incomplete command.|Ambiguous command:\s\s"\w"')
            match = re.search(regex, out)
            if match:
                err = match.group()
                if strict == False:
                    print(f"При выплнении команды -{command}- на устройстве {self.ip} возникла ошибка -> {err}")
                elif strict == True:
                    raise ValueError(f"При выплнении команды -{command}- на устройстве {self.ip} возникла ошибка -> {err}")
            else:

                out_correct += out
        self.telnet.write(b'end\n')
        time.sleep(0.5)
        res = self.telnet.read_very_eager().decode('ascii')
        fin = out_correct+res

        return fin
