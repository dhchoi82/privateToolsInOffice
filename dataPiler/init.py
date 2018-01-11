#!/usr/bin/python3

import sqlite3

def initDB():
    with sqlite3.connect('data.sqlite') as con, open('init.sql','r') as f:
        cur = con.cursor()
        sql = f.read()
        con.executescript(sql)

if __name__ == "__main__":
    initDB()
