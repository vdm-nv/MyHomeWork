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


def get_int_vlan_map(config_filename):
    result = ()
    access = {}
    trunk = {}
    
    with open(config_filename) as f:
        for line in f:
            if 'FastEth' in line:           # ищем FastEth
                intf_a = line.split()[1]    # отбираем все FastEthernetХ/Х
            elif 'access vlan' in line:     # если есть acces vlan в строке
                vl_a = line.split()[-1]     # присваиваем последнее значение строки , это номер вилана = 10 или 20 и т.д.
                access[intf_a] = int(vl_a)  # добавляем значение в словарь access,где ключ intf,а значение -vlan(число)

            elif 'mode access' in line:     # ищем по mode access
                 vl_b = 1
                 access[intf_a] = vl_b       # добавляем в словарь access, оставшиеся интерфейсы со значение 1

            elif 'allowed vlan' in line:
                 vl_с = line.split()        # разбивает строку на части 
                 vlvl = []
                 vl = vl_с[-1].split(',')   # забираем на список заняения ['100', '200'] 
                 for i in vl:
                    vlvl.append(int(i))    # добавляем в новый список числа из списка vl
                    trunk[intf_a] = vlvl       # создаем словарь trunk, где ключ intf_a, а значение список чисел vlvl
                    result = (access, trunk)   # создаем кортеж из словарей access, trunk
         return result
