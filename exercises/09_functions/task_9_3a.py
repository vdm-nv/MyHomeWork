# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
result = ()
access = {}
trunk = {}

def get_int_vlan_map(config_filename):
        with open(config_filename) as f:
            for line in f:
                if 'FastEth' in line:           # ищем fasteth
                    intf_a = line.split()[1]    #
                elif 'access vlan' in line:     # и если есть acces vl
                    vl_a = line.split()[-1]     #
                    access[intf_a] = int(vl_a)  # добавляем значение access intf и vlan в числовом значении

                elif 'mode access' in line:
                    vl_b = 1
                    access[intf_a] = vl_b

                elif 'allowed vlan' in line:
                     vl_с = line.split()        # разбивает строку на части 
                     vlvl = []
                     vl = vl_с[-1].split(',')   # забираем 
                     for i in vl:
                         vlvl.append(int(i))
                     trunk[intf_a] = vlvl
                     result = (access, trunk)
            return result
