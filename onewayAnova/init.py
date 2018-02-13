#!/usr/bin/python3
from os.path import isfile

def setInput():
    csvFilename = 'inputList.csv'
    dumpContents = '''value,factor
4.96,A
4.41,C
4.93,B
4.36,C
4.82,B
4.97,A
4.68,C
4.48,C
4.9,A
5.02,A
4.76,B
5.08,A
5.03,A
4.57,C
4.36,C
5,A
4.37,C
5.15,A
5.1,A
4.92,B
5.1,A
4.77,B
4.37,C
4.81,A
5.11,A
4.24,C
4.69,B
5.08,A
4.32,C
4.59,C
4.64,C
4.78,C
5.01,B
5.04,B
4.65,B
5.2,B
4.89,B
4.74,B
5.1,B
4.3,C
4.88,A
4.64,C
4.85,A
4.46,C
4.53,C
4.33,C
5.01,A
4.77,B
4.86,B
4.71,C
4.71,B
4.51,C
4.53,C
4.38,C
4.91,A
5.2,A
4.42,C
4.74,B
4.63,C
'''
    
    if not isfile(csvFilename):
        with open(csvFilename,'w') as f:
            f.write(dumpContents)

if __name__ == '__main__':
    setInput()
