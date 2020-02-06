# -*- coding: utf-8 -*-
'''
Задание 20.3

Создать функцию send_command_to_devices, которая отправляет
разные команды show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* commands_dict - словарь в котором указано на какое устройство отправлять какую команду. Пример словаря - commands
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh arp
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  192.168.100.1          76   aabb.cc00.6500  ARPA   Ethernet0/0
Internet  192.168.100.2           -   aabb.cc00.6600  ARPA   Ethernet0/0
Internet  192.168.100.3         173   aabb.cc00.6700  ARPA   Ethernet0/0
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down


Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml и словаре commands
'''

from concurrent.futures import ThreadPoolExecutor, as_completed
from pprint import pprint
from datetime import datetime
import time
import logging

import yaml
from netmiko import ConnectHandler, NetMikoAuthenticationException



logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
        format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
        level=logging.INFO)

def send_command_to_devices(devices, commands_dict, filename, limit=3):
    start_msg = '===> {} Connection: {}'
    received_msg = '<=== {} Received: {}'
    ip = devices['ip']
    logging.info(start_msg.format(datetime.now().time(), ip))

    with ConnectHandler(**devices) as ssh:
        ssh.enable()
        res01 = ssh.send_command('sh run | se hostname')
        result = ssh.send_command(commands_dict)
        ress = '\n'+res01[9:]+'#'+commands_dict+'\n'+result
        print(ress)
        logging.info(received_msg.format(datetime.now().time(), ip))

    with open(filename, 'a') as f:
        f.write(ress)



commands = {'192.168.100.1': 'sh ip int br',
            '192.168.100.2': 'sh arp',
            '192.168.100.3': 'sh ip int br'}


if __name__ == '__main__':
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        future_list = []
        for device in devices:
            ip = device['ip']
            for key,value in commands.items():
                if ip == key:
                    comm = value

                    future = executor.submit(send_command_to_devices, device, comm, 'out_3.txt')
                    future_list.append(future)
        for f in as_completed(future_list):
            resultt = f.result()
