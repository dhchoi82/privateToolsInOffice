#!/usr/bin/python3

import sqlite3

with sqlite3.connect('data.sqlite') as con, open('init.sql','r') as f:
    cur = con.cursor()
    sql = f.read()
    con.executescript(sql)
