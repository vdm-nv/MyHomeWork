import re
import glob
import sqlite3
import yaml

res =[]

files = glob.glob('sw*.txt')

regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

for item in files:
    with open(item) as data:
        for line in data:
            match = regex.search(line)
            if match:
                m = match.groups()
                n = item[:3]
                mm = m + (n,)
                res.append(mm)

conn = sqlite3.connect('dhcp_snooping.db')

for row in res:
        try:
            with conn:
                query = '''insert into dhcp (mac, ip, vlan, interface, switch)
                           values (?, ?, ?, ?, ?)'''
                conn.execute(query, row)
        except sqlite3.IntegrityError as e:
            print('При добавлении данных: ', row, 'Возникла ошибка: ', e)

with open('switches.yml') as f:
        templates = yaml.safe_load(f)

for k,v in templates['switches'].items():
    try:
        with conn:
            query = '''insert into switches (hostname, location) values (?,?)'''
            conn.executemany(query, tuple(templates['switches'].items()))
    except sqlite3.IntegrityError as e:
        print('При добавлении данных: ',(k,v), 'Возникла ошибка: ', e)

