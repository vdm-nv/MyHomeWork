# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

'''


def convert_ranges_to_ip_list(list_with_ip):
 
    res =[]
 
    fir, sec, last = list_with_ip
    res.append(fir)
    seco = sec.split('.')
    z1,z2,z3,z4 = seco
    second = z4.split('-')
    start = second[0]
    end = second[-1]
    a = '.'
    for x in range(int(start), int(end)+1):
        res.append(z1+a+z2+a+z3+a+ str(x))

    las = last.split('-')
    startt = las[0].split('.')[-1]
    endd = las[-1].split('.')[-1]
    b = las[0].split('.')
    ff,ss,tri,_ = b
    for z in range(int(startt),int(endd) +1):
        res.append(ff+a+ss+a+tri+a+ str(z))
    return res

