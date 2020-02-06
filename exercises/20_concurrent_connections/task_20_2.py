# -*- coding: utf-8 -*-
'''
Задание 20.2

Создать функцию send_show_command_to_devices, которая отправляет
одну и ту же команду show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
'''
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import repeat
from datetime import datetime
import time
from pprint import pprint

import netmiko,yaml

logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
        format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
        level=logging.INFO)

def send_show_command_to_devices(devices, command, filename, limit=3):
    start_msg = '===> {} Connection to: {}'
    received_msg = '<=== {} Received from: {}'

    ip = devices['ip']
    logging.info(start_msg.format(datetime.now().time(), ip))
    with netmiko.ConnectHandler(**devices) as ssh:
        ssh.enable()
        res01 = ssh.send_command('sh run | se hostname')
        result = ssh.send_command(command)
        ress = '\n'+res01[9:]+'#'+command+'\n'+result
        print(ress)
    with open(filename, 'a') as f:
        print(f'Записываю результат в файл *** from {ip}')
        f.write(ress)
        logging.info(received_msg.format(datetime.now().time(), ip))

with open('devices.yaml') as f:
    ddevices = yaml.safe_load(f)

with ThreadPoolExecutor(max_workers=3) as executor:
    command = 'sh ip int b'
    future_list = []
    for dev in ddevices:
        future = executor.submit(send_show_command_to_devices, dev, command, 'result.txt')
        future_list.append(future)
    for f in as_completed(future_list):
        result = f.result()


