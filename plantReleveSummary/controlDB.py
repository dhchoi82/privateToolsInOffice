#!/usr/bin/python3

import sqlite3, csv
from os.path import isfile
from math import log

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
            f.write('unitNum,releveNum,name,cover\n1,1,koreanName1,3\n1,2,koreanName2,5')
    
    with sqlite3.connect(dbFile) as con, open(csvFilename,'r',encoding="utf-8") as inputFile, open('sql/refresh.sql','r') as sqlFile:
        
        # (2)
        sql = sqlFile.read()
        con.executescript(sql)
        
        # (3)
        cur = con.cursor()
        inputDict = csv.DictReader(inputFile, delimiter=",")
        sql = '''INSERT INTO inputList(unitNum, releveNum, name, cover)
            VALUES (:unitNum, :releveNum, :name, :cover)'''
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

## 함수: makeUnitNCD, 입력값: unit 번호, 반환값: [종명, NCD] 리스트
# DB에서 inputList 테이블의 unitNum 값이 입력된 unitNumber와 같은 레코드를 찾아
# `NCD = [unit 내 해당 종 (0포함) 피도의 평균] * [unit 내 해당 종 빈도]`를 계산하여
# 종별 NCD 값의 리스트를 반환
def makeUnitNCD(unitNumber):
    with sqlite3.connect(dbFile) as con:
        sql = '''SELECT COUNT(*)
            FROM (SELECT DISTINCT releveNum
                FROM inputList WHERE unitNum = ?
            )''' # 해당 unit의 조사구 개수를 구함
        cur = con.cursor()
        cur.execute(sql, (unitNumber,))
        releveCount = cur.fetchone()
        
        sql = 'SELECT name, SUM(cover) * COUNT(*) / ? FROM inputList WHERE unitNum = ? GROUP BY name' # 해당 unit의 NCD를 계산
        cur.execute(sql, (releveCount[0]**2, unitNumber))
        return cur.fetchall()

## 함수: makeRncdList, 입력값: 없음, 반환값: [unit 번호, [종명, NCD, rNCD]] 리스트
# DB에서 inputList 테이블의 unitNum 값 종류를 모두 찾아
# `rNCD = NCD / NCDmax`를 계산하여
# unit 별 NCD, rNCD 값의 리스트를 반환
def makeRncdList():
    rncdList = []
    
    with sqlite3.connect(dbFile) as con:
        sql = 'SELECT DISTINCT unitNum FROM inputList' # unit 번호 목록 생성
        cur = con.cursor()
        
        for unit in cur.execute(sql):
            ncds = makeUnitNCD(unit[0]) # 해당 unit의 NCD 리스트 생성
            ncdMax = max([x[1] for x in ncds]) # NCD 최댓값 계산
            rncdRow = [(x[0], x[1], x[1]/ncdMax*100) for x in ncds] # rNCD 포함 리스트 생성
            rncdList.append([unit[0],rncdRow]) # 해당 unit에서 구한 리스트 추가
    
    return rncdList

def elementShannonIndex(cover_i, sum_cover):
    p_i = cover_i / sum_cover
    element = p_i * log(p_i)
    return element

def makeShannonIndexList():
    with sqlite3.connect(dbFile) as con:
        con.create_function("ElementH", 2, elementShannonIndex)
        sql = '''SELECT releveNum, -SUM(Hi)
            FROM (SELECT id, releveNum, ElementH(cover, coverSum) AS Hi
            FROM inputList LEFT JOIN (
                SELECT releveNum AS releveId, SUM(cover) AS coverSum
                FROM inputList GROUP BY releveNum
            ) ON inputList.releveNum=releveId
        ) GROUP BY releveNum
        '''
        cur = con.cursor()
        cur.execute(sql)
        
        return cur.fetchall()

if __name__ == "__main__":
    initDB()
    setInput()
    print(makeShannonIndexList())
