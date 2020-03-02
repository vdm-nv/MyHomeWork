# -*- coding: utf-8 -*-
'''
Задание 21.5a

Создать функцию configure_vpn, которая использует шаблоны из задания 21.5 для настройки VPN на маршрутизаторах на основе данных в словаре data.

Параметры функции:
* src_device_params - словарь с параметрами подключения к устройству
* dst_device_params - словарь с параметрами подключения к устройству
* src_template - имя файла с шаблоном, который создает конфигурацию для одной строны туннеля
* dst_template - имя файла с шаблоном, который создает конфигурацию для второй строны туннеля
* vpn_data_dict - словарь со значениями, которые надо подставить в шаблоны

Функция должна настроить VPN на основе шаблонов и данных на каждом устройстве.
Функция возвращает вывод с набором команд с двух марушртизаторов (вывод, которые возвращает send_config_set).

При этом, в словаре data не указан номер интерфейса Tunnel, который надо использовать.
Номер надо определить самостоятельно на основе информации с оборудования.
Если на маршрутизаторе нет интерфейсов Tunnel, взять номер 0, если есть взять ближайший свободный номер,
но одинаковый для двух маршрутизаторов.

Например, если на маршрутизаторе src такие интерфейсы: Tunnel1, Tunnel4.
А на маршрутизаторе dest такие: Tunnel2, Tunnel3, Tunnel8.
Первый свободный номер одинаковый для двух маршрутизаторов будет 9.
И надо будет настроить интерфейс Tunnel 9.

Для этого задания нет теста!
'''
import yaml,netmiko
import logging
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from pprint import pprint

# эта строка указывает ,что лог-сообщения paramiko юудут выводиться
# только если они уровня WARNING и выше
logging.getLogger("paramiko").setLevel(logging.WARNING)

logging.basicConfig(
        format = '%(threadName)s %(name)s %(levelname)s: %(message)s',
        level=logging.INFO)

def configure_vpn(src_device_params, dst_device_params, src_template, dst_template, vpn_data_dict):
    start_msg = '===> {} Connection to: {}'
    received_msg = '<=== {} Received from: {}'

    env = Environment(
                loader=FileSystemLoader('templates'),
                trim_blocks=True,
                lstrip_blocks=True)
    template1 = env.get_template(src_template)
    res1 = template1.render(vpn_data_dict)

    template2 = env.get_template(dst_template)
    res2 = template2.render(vpn_data_dict)

    print('Подключаюсь к устройству {}'.format(src_device_params['ip']))
    ssh1 = netmiko.ConnectHandler(**src_device_params)
    ssh1.enable()
    out1 = ssh1.send_config_set(res1.split('\n')) #res1 -- MUST BE LIST not str!!
    logging.info(received_msg.format(datetime.now().time(), dst_device_params['ip']))

    print('Подключаюсь к устройству {}'.format(dst_device_params['ip']))
    ssh2 = netmiko.ConnectHandler(**dst_device_params)
    ssh2.enable()
    out2 = ssh2.send_config_set(res2.split('\n'))
    logging.info(received_msg.format(datetime.now().time(), dst_device_params['ip']))
    return [out1, out2]

if __name__ == "__main__":
    with open('data_files/devices.yaml') as f:
        devices = yaml.safe_load(f)
    r1 = devices[0]
    r2 = devices[1]

    data = {
        'tun_num': 10,
        'wan_ip_1': '192.168.100.1',
        'wan_ip_2': '192.168.100.2',
        'tun_ip_1': '10.0.1.1 255.255.255.252',
        'tun_ip_2': '10.0.1.2 255.255.255.252'
    }

    pprint(configure_vpn(r1, r2, 'gre_ipsec_vpn_1.txt','gre_ipsec_vpn_2.txt', data))

