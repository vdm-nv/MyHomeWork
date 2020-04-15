# -*- coding: utf-8 -*-

'''
Задание 26.3a

Изменить класс IPAddress из задания 26.3.

Добавить два строковых представления для экземпляров класса IPAddress.
Как дожны выглядеть строковые представления, надо определить из вывода ниже:

Создание экземпляра
In [5]: ip1 = IPAddress('10.1.1.1/24')

In [6]: str(ip1)
Out[6]: 'IP address 10.1.1.1/24'

In [7]: print(ip1)
IP address 10.1.1.1/24

In [8]: ip1
Out[8]: IPAddress('10.1.1.1/24')

In [9]: ip_list = []

In [10]: ip_list.append(ip1)

In [11]: ip_list
Out[11]: [IPAddress('10.1.1.1/24')]

In [12]: print(ip_list)
[IPAddress('10.1.1.1/24')]

Для этого задания нет теста!
'''
class IPAddress:
    def __init__(self, addr):
        temp = addr.split('/')
        if len(temp[0].split('.')) == 4:
            self.ip = temp[0]
        else:
            raise ValueError('Incorrect IPv4 address')

        for i in temp[0].split('.'):
            if not i.isdigit() or not 0 <= int(i) <=255:
                raise ValueError('Incorrect IPv4 address')
            else:
                self.ip = temp[0]

        if 8 <= int(temp[1]) <= 32:
            self.mask = int(temp[1])
        else:
            raise ValueError('Incorrect mask')
        print("\nАтрибуты ip и mask")

    def __str__(self):
        return f"IP address: {self.ip}"

    def __repr__(self):
        return f"IP address('{self.ip}')"

if __name__ == "__main__":
    ip1 = IPAddress('10.1.1.1/24')
    print("assign ip1 = IPAddress('10.1.1.1/24')", end='\n\n')
    print(str(ip1), end='\n\n')
    print(ip1, end='\n\n')
    ip_list = []
    ip_list.append(ip1)
    ip_list
    print(ip_list, end='\n')
