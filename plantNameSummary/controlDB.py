#!/usr/bin/python3

import sqlite3
from os.path import isfile

dbFile = 'data.sqlite'

## 함수: initDB, 입력값: 없음, 반환값: 없음
# 현재 디렉토리에서 DB파일 존재 확인 후 없으면 새로 생성
def initDB():
    if not isfile(dbFile):
        with sqlite3.connect(dbFile) as con, open('init.sql','r') as f:
            sql = f.read()
            con.executescript(sql)

## 함수: getList, 입력값: 없음, 반환값: 리스트
# DB에서 inputList 테이블의 name 값이 speciesList 테이블의 korean에 존재하면
# 해당 종의 정보 리스트를 반환
def getList():
    with sqlite3.connect(dbFile) as con, open('getList.sql','r') as f:
        sql = f.read()
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

if __name__ == "__main__":
    initDB()
