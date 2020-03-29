# -*- coding: utf-8 -*-

'''
Задание 25.2a

Скопировать класс CiscoTelnet из задания 25.2 и изменить метод send_show_command добавив два параметра:

* parse - контролирует то, будет возвращаться обычный вывод команды или список словарей, полученные после обработки с помощью TextFSM. При parse=True должен возвращаться список словарей, а parse=False обычный вывод
* templates - путь к каталогу с шаблонами



Пример создания экземпляра класса:

In [1]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [2]: from task_25_2a import CiscoTelnet

In [3]: r1 = CiscoTelnet(**r1_params)

Использование метода send_show_command:
In [4]: r1.send_show_command('sh ip int br', parse=False)
Out[4]: 'sh ip int br\r\nInterface                  IP-Address      OK? Method Status                Protocol\r\nEthernet0/0                192.168.100.1   YES NVRAM  up                    up      \r\nEthernet0/1                192.168.200.1   YES NVRAM  up                    up      \r\nEthernet0/2                190.16.200.1    YES NVRAM  up                    up      \r\nEthernet0/3                192.168.130.1   YES NVRAM  up                    up      \r\nEthernet0/3.100            10.100.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.200            10.200.0.1      YES NVRAM  up                    up      \r\nEthernet0/3.300            10.30.0.1       YES NVRAM  up                    up      \r\nLoopback0                  10.1.1.1        YES NVRAM  up                    up      \r\nLoopback55                 5.5.5.5         YES manual up                    up      \r\nR1#'

In [5]: r1.send_show_command('sh ip int br', parse=True)
Out[5]:
[{'intf': 'Ethernet0/0',
  'address': '192.168.100.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/1',
  'address': '192.168.200.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/2',
  'address': '190.16.200.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3',
  'address': '192.168.130.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3.100',
  'address': '10.100.0.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3.200',
  'address': '10.200.0.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Ethernet0/3.300',
  'address': '10.30.0.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Loopback0',
  'address': '10.1.1.1',
  'status': 'up',
  'protocol': 'up'},
 {'intf': 'Loopback55',
  'address': '5.5.5.5',
  'status': 'up',
  'protocol': 'up'}]
'''
import textfsm,clitable
import telnetlib
import time,os
from pprint import pprint

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
            attributes = {'Command': 'sh ip int br' , 'Vendor': 'cisco_ios'}
            cli_table = clitable.CliTable('index', templates)
            cli_table.ParseCmd(output, attributes)
            data_rows = [list(row) for row in cli_table]
            res = []
            for d in data_rows:
                    res.append(dict(zip(list(cli_table.header),d)))
            return res
        else:
            return output

if __name__ == '__main__':
    r1_params = {'ip': '192.168.100.1',
                 'username': 'cisco',
                 'password': 'cisco',
                 'secret': 'cisco'}

    r1 = CiscoTelnet(**r1_params)
    print('#'*79)
    print('Result without PARSING!\n')
    pprint(r1.send_show_command('sh ip int br'))
    print('#'*79)
    print('Result with Parse=True\n')
    pprint(r1.send_show_command('sh ip int br',parse=True))
    print('#'*79)

