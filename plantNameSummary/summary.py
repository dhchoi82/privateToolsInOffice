#!/usr/bin/python3

import csv
from controlDB import getList

## 함수: makeCSV, 입력값: (종 리스트,출력파일 이름), 반환값: csv 파일 내용 문자열
def makeCSV(fetchedList,fileName='resultList.csv'):
    with open(fileName,'w',newline='') as csvfile:
        head = ['familyName','familyKorean','genusName','specificEpithet',
            'intraClass','intraspecificName','specificKorean','authorSpecific',
            'authorIntraspecific']
        writerObject = csv.writer(csvfile)
        
        writerObject.writerow(head)
        writerObject.writerows(fetchedList)
    
    with open(fileName,'r') as csvfile:
        return csvfile.read()

if __name__ == '__main__':
    print(makeCSV(getList()))
