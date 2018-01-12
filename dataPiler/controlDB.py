#!/usr/bin/python3

import sqlite3
from os.path import isfile

dbFile = 'data.sqlite'

def initDB():
    if not isfile(dbFile): # 데이터베이스 존재 확인 후 없으면 새로 생성
        with sqlite3.connect(dbFile) as con, open('init.sql','r') as f:
            sql = f.read()
            con.executescript(sql)

def getDB(table): # table 변수와 이름이 같은 DB 테이블이 있으면 전체 자료 반환
    with sqlite3.connect(dbFile) as con:
        cur = con.cursor()
        
        if table in ("data","sorts","sources"):
            sql = "SELECT * FROM {}".format(table)
            cur.execute(sql)
            return cur.fetchall()
        else:
            return None

def pickRecord(table,id): # table 변수와 이름이 같은 DB 테이블에서 no=id인 자료 반환
    with sqlite3.connect(dbFile) as con:
        cur = con.cursor()
        
        if table in ("data","sorts","sources"):
            sql = "SELECT * FROM {} WHERE no=?".format(table)
            cur.execute(sql,(id,))
            return cur.fetchone()
        else:
            return None

def delRecord(table,id): # table 변수와 이름이 같은 DB 테이블에서 no=id인 자료 삭제
    with sqlite3.connect(dbFile) as con:
        cur = con.cursor()
        
        if table in ("data","sorts","sources"):
            sql = "DELETE FROM {} WHERE no=?".format(table)
            cur.execute(sql,(id,))
            return (pickRecord(table,id) == None)
        else:
            return False

def addRecord(table,inputs): # table 변수와 이름이 같은 DB 테이블에 inputs 변수의 자료 생성
    pass

if __name__ == "__main__":
    initDB()
