# -*- coding: utf-8 -*-

'''
Задание 25.1d

Изменить класс Topology из задания 25.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще нет в топологии
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение "Cоединение с одним из портов существует"


Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Cоединение с одним из портов существует


'''
from pprint import pprint

topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}

class Topology:
    def __init__(self, top):
        self.topology = self._normalize(top)

    def _normalize(self, top):
        self.res = {}
        for key,value in top.items():
            if value not in self.res.keys():
                self.res[key] = value
        return self.res

    def add_link(self, port01, port02):
        flag = True
        for k,v in list(self.res.items()):
            if port01 == k and port02 == v:
                print('Такое соединение существует')
                flag = False
            elif port01 == k or port02 == v:
                print('Cоединение с одним из портов существует')
                flag = False
        if flag:
            self.res.update({port01: port02})

if __name__ == "__main__":
    top = Topology(topology_example)
    pprint(top.topology)
    print("\nadd new link ('R1', 'Eth0/4'), ('R7', 'Eth0/0')")
    top.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
    pprint(top.topology)
    print("\nadd new link AGAIN ('R1', 'Eth0/4'), ('R7', 'Eth0/0')")
    top.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
    print("\nadd new link  with exist port('R1', 'Eth0/4'), ('R7', 'Eth0/5')")
    top.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))

