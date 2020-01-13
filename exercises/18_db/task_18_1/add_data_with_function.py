import re
import glob
import sqlite3
import yaml,os

files = glob.glob('sw*.txt')
db_filename = 'dhcp_snooping.db'

def create_connection(db_name):
    '''
    Функция создает соединение с БД db_name
    и возвращает его
    '''
    connection = sqlite3.connect(db_filename)
    return connection

def data_for_dhcp(ffiles):
    res =[]
    regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

    for item in ffiles:
        with open(item) as data:
            for line in data:
                match = regex.search(line)
                if match:
                    m = match.groups()
                    n = item[:3]
                    mm = m + (n,)
                    res.append(mm)
    return res

def data_for_switches(ff):
    with open(ff) as f:
        templates = yaml.safe_load(f)
    return templates

def write_data_to_dhcp(connection, query, data):
    '''
    Функция ожидает аргументы:
    * connection - соединение с БД
    * query - запрос, который нужно выполнить
    * data - данные, которые надо передать в виде списка кортежей

    Функция пытается записать все данные из списка data.
    Если данные удалось записать успешно, изменения сохраняются в БД
    и функция возвращает True.
    Если в процессе записи возникла ошибка, транзакция откатывается
    и функция возвращает False.
    '''
    print('Добавляю данные в таблицу dhcp...')

    for row in data:
        try:
            with conn:
                conn.execute(query, row)
        except sqlite3.IntegrityError as e:
            print('При добавлении данных: ', row, 'Возникла ошибка: ', e)
    #        return False
    #    else:
    return True

def write_data_to_switches(connection, query, data):
    print('Добавляю данные в таблицу switches...')

    for k,v in templates['switches'].items():
        try:
            with conn:
                conn.execute(query,(k,v))
        except sqlite3.IntegrityError as e:
            print('При добавлении данных: ',(k,v), 'Возникла ошибка: ', e)

     #   else:
     #       return True
    return True

if __name__ == '__main__':
    res = data_for_dhcp(files)
    templates = data_for_switches('switches.yml')
    conn =  create_connection(db_filename)
    query_dhcp = '''insert into dhcp (mac, ip, vlan, interface, switch)
               values (?, ?, ?, ?, ?)'''
    query_sw = '''insert into switches (hostname, location) values (?,?)'''

    write_data_to_dhcp(conn, query_dhcp, res)
    write_data_to_switches(conn, query_sw, templates)
