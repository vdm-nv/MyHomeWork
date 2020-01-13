import sqlite3
import os

db_filename = 'dhcp_snooping.db'
schema_filename = 'dhcp_snooping_schema.sql'
db_exists = os.path.exists(db_filename)

def create_connection(db_name):
    '''
    Функция создает соединение с БД db_name
    и возвращает его
    '''
    connection = sqlite3.connect(db_filename)
    return connection

if __name__ == '__main__':

    conn =  create_connection(db_filename)

    if not db_exists:
        print('Создаю базу данных...')
        with open(schema_filename, 'r') as f:
            schema = f.read()
        conn.executescript(schema)
    else:
        print('База данных сущестует!')




