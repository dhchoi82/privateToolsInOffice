#!/usr/bin/python3
from os.path import isfile

def setInput():
    csvFilename = 'inputList.csv'
    dumpContents = '''factorA,factorB
a,A
a,B
a,A
b,A
b,A
c,A
c,B
c,B
a,B
b,A
a,A
b,B
c,C
c,C
c,A
c,B
a,C
a,C
b,C
c,C
c,C
c,A
c,B
a,C
a,C
b,C
c,C
c,C
c,A
c,B
a,C
a,C
b,C
c,C
c,C
c,A
a,B
a,A
b,A
b,A
c,A
c,B
c,B
b,B
b,C
b,B
b,B
b,C
c,C
c,B
b,B
b,C
a,B
a,C
a,A
b,A
a,B
'''
    
    if not isfile(csvFilename):
        with open(csvFilename,'w') as f:
            f.write(dumpContents)

if __name__ == '__main__':
    setInput()
