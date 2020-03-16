# -*- coding: utf-8 -*-
'''
Задание 22.5

Создать функцию send_and_parse_command_parallel.

Функция send_and_parse_command_parallel должна запускать в параллельных потоках функцию send_and_parse_show_command из задания 22.4.

В этом задании надо самостоятельно решить:
* какие параметры будут у функции
* что она будет возвращать


Теста для этого задания нет.
'''
import netmiko,yaml
from concurrent.futures import ThreadPoolExecutor, as_completed
from task_22_4 import send_and_parse_show_command
from pprint import pprint

result = []

def send_and_parse_command_parallel(devices, command):
    with ThreadPoolExecutor(max_workers=3) as executor:
        future_list = []
        for dev in devices:
            future = executor.submit(send_and_parse_show_command, dev, command, 'templates')
            future_list.append(future)
        for f in as_completed(future_list):
            result.append(f.result())
    return result

if __name__ == "__main__":
    with open('devices.yaml') as f:
        ddevices = yaml.safe_load(f)
    pprint(send_and_parse_command_parallel(ddevices, 'sh ip int b'))

