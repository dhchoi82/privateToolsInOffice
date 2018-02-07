#!/usr/bin/python3
from os.path import isfile

def setInput():
    csvFilename = 'inputList.csv'
    dumpContents = '''groupA,groupB
2.79,2.89
3.51,3.11
3.03,2.49
4.41,2.96
3.32,2.75
3.8,2.76
3.38,2.64
3.94,2.78
4.25,2.87
4.32,2.76
2.91,3.1
3.1,2.58
3.62,3.07
3.9,2.27
3.35,3.49
3.62,2.65
3.67,2.66
3.34,3.22
4.06,2.78
3.37,2.6
3.25,2.63
3.06,3.08
2.95,2.88
4.11,2.73
3.46,2.67
3.81,3.03
3.66,3.29
3.78,2.46
3.65,2.92
3.47,3.04
'''
    
    if not isfile(csvFilename):
        with open(csvFilename,'w') as f:
            f.write(dumpContents)

if __name__ == '__main__':
    setInput()
