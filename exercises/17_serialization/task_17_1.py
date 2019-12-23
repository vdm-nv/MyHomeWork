# -*- coding: utf-8 -*-
'''
Задание 17.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv), в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
'''

import glob
import re
import csv

sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']

def parse_sh_version(outputs):
    regex = (r'.+, Version (\d+.\d\S+), '
             r'(.+\s){7}.+ '				#перебираем кол-во строк с переносом строки \n
             r'uptime is((?: \d+ \w+,){2} \d+ \w+)'
             r'\s.+\s.+ file is "(\S+:\S+\.\w+)"')

    res = re.search(regex, outputs)
    ios = res.group(1)
    upt = res.group(3).lstrip()				#убираем левый пробел
    platf = res.group(4)
    result = (ios,platf,upt)
    return result

def write_inventory_to_csv(data_filenames, csv_filename):

        r1,r2,r3 = '','',''
        res1,res2,res3 = [],[],[],
        finres = []

        for item in sh_version_files:
            if r2 in item:
                r2 = 'r2'
                with open(item) as f:
                    sh_ver_r2 = f.read()			#считываем файл в одну строку
                    res2 = list(parse_sh_version(sh_ver_r2))	#запускам функцию парсинга и присваиваем вывод списку
                    res2.insert(0,r2)				#добавлем первое значение(0) - из имени файла

            elif r3 in item:
                r3 = 'r3'
                with open(item) as f:
                    sh_ver_r3 = f.read()
                    res3=list(parse_sh_version(sh_ver_r3))
                    res3.insert(0,r3)

            elif r1 in item:
                r1 = 'r1'
                with open(item) as f:
                    sh_ver_r1 = f.read()
                    res1=list(parse_sh_version(sh_ver_r1))
                    res1.insert(0,r1)

        finres.append(list(headers))
        finres.append(res1)
        finres.append(res2)
        finres.append(res3)
        with open(csv_filename, 'w') as f:
            writer = csv.writer(f)
            for row in finres:
                writer.writerow(row)
