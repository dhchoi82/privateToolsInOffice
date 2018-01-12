#!/usr/bin/python3

import sqlite3
from os.path import isfile

dbFile = 'data.sqlite'

def initDB():
    if not isfile(dbFile): # 데이터베이스 존재 확인 후 없으면 새로 생성
        with sqlite3.connect(dbFile) as con, open('init.sql','r') as f:
            cur = con.cursor()
            sql = f.read()
            con.executescript(sql)

if __name__ == "__main__":
    initDB()
