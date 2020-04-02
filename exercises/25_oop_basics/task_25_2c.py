# -*- coding: utf-8 -*-

'''
Задание 25.2b

Скопировать класс CiscoTelnet из задания 25.2a и добавить метод send_config_commands.


Метод send_config_commands должен уметь отправлять одну команду конфигурационного режима или список команд.
Метод должен возвращать вывод аналогичный методу send_config_set у netmiko (пример вывода ниже).

Пример создания экземпляра класса:
In [1]: from task_25_2b import CiscoTelnet

In [2]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

Использование метода send_config_commands:

In [5]: r1.send_config_commands('logging 10.1.1.1')
Out[5]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#logging 10.1.1.1\r\nR1(config)#end\r\nR1#'

In [6]: r1.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255'])
Out[6]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#interface loop55\r\nR1(config-if)#ip address 5.5.5.5 255.255.255.255\r\nR1(config-if)#end\r\nR1#'

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
