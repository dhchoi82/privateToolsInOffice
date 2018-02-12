#!/usr/bin/python3

import csv, codecs
from controlDB import setInput, getList, makeRncdList

## 함수: makeCSV, 입력값: (종 리스트,출력파일 이름), 반환값: csv 파일 내용 문자열
def makeSpeciesCSV(fetchedList,fileName='resultList(species).csv'):
    with codecs.open(fileName, mode='w', encoding='utf-8') as csvfile:
        head = ['familyName','familyKorean','genusName','specificEpithet',
            'intraClass','intraspecificName','specificKorean','authorSpecific',
            'authorIntraspecific']
        writerObject = csv.writer(csvfile)
        
        writerObject.writerow(head)
        writerObject.writerows(fetchedList)
    
    with codecs.open(fileName, mode='r', encoding='utf-8') as csvfile:
        return csvfile.read()

def makeCounts(summaryList):
    taxaNum = len(summaryList)
    subspNum = 0
    varNum = 0
    forNum = 0
    
    family = set()
    genus = set()
    
    for item in summaryList:
        family.add(item[0])
        genus.add(item[2])
        if item[4] == 'subsp.': subspNum += 1
        elif item[4] == 'var.': varNum += 1
        elif item[4] == 'f.': forNum += 1
    
    spNum = taxaNum - (subspNum + varNum + forNum)
    input("{}과 {}속 {}종 {}아종 {}변종 {}품종 {}분류군".format(
        len(family), len(genus), spNum, subspNum, varNum, forNum, taxaNum
        ))

def showRncdList():
    for unitNumber, unitList in makeRncdList():
        print(unitNumber)
        for species in unitList:
            print(species)
        input()

def makeRncdCSV(fileName='resultList(rNCD).csv'):
    with codecs.open(fileName, mode='w', encoding='utf-8') as csvfile:
        head = ['unitNumber','speciesName','NCD','rNCD']
        writerObject = csv.writer(csvfile)
        
        writerObject.writerow(head)
        for unitNumber, unitList in makeRncdList():
            for species in unitList: 
                writerObject.writerow([unitNumber,]+list(species))
    
    with codecs.open(fileName, mode='r', encoding='utf-8') as csvfile:
        return csvfile.read()

if __name__ == '__main__':
    setInput()
    summaryList = getList()
    print(makeSpeciesCSV(summaryList))
    makeCounts(summaryList)
    showRncdList()
    print(makeRncdCSV())
