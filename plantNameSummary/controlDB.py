#!/usr/bin/python3

import sqlite3, csv
from os.path import isfile

dbFile = 'data.sqlite'

## 함수: initDB, 입력값: 없음, 반환값: 없음
# 현재 디렉토리에서 DB파일 존재 확인 후 없으면 새로 생성
def initDB():
    if not isfile(dbFile):
        with sqlite3.connect(dbFile) as con, open('sql/init.sql','r') as f:
            sql = f.read()
            con.executescript(sql)

## 함수: setInput, 입력값: 없음, 반환값: 없음
# 현재 디렉토리에서 'inputList.csv' 파일이 없으면 새로 생성 (1)
# DB inputList 테이블을 초기화한 뒤, (2)
# 'inputList.csv' 파일에서 name 열의 모든 값을
# DB inputList 테이블에 추가 (3)
def setInput():
    csvFilename = 'inputList.csv'
    
    # (1)
    if not isfile(csvFilename):
        with open(csvFilename,'w') as f:
            f.write('name\nkoreanName1\nkoreanName2')
    
    with sqlite3.connect(dbFile) as con, open(csvFilename,'r',encoding="utf-8") as inputFile, open('sql/refresh.sql','r') as sqlFile:
        
        # (2)
        sql = sqlFile.read()
        con.executescript(sql)
        
        # (3)
        cur = con.cursor()
        inputDict = csv.DictReader(inputFile, delimiter=",")
        sql = 'INSERT INTO inputList(name) VALUES (:name)'
        cur.executemany(sql, inputDict)

## 함수: getList, 입력값: 없음, 반환값: 리스트
# DB에서 inputList 테이블의 name 값이 speciesList 테이블의 korean에 존재하면
# 해당 종의 정보 리스트를 반환
def getList():
    with sqlite3.connect(dbFile) as con, open('sql/getList.sql','r') as f:
        sql = f.read()
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

if __name__ == "__main__":
    initDB()
    setInput()
