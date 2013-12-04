#!/usr/bin/env python
import sys
def creatDic():
    freqDic = {}
    with open('sortedList', 'r') as sortedList:
        for line in sortedList:
            line = line.strip().split('\t')
            freqDic[int(line[0])] = int(line[1])
    return freqDic

def read_input(inFile):
    for line in inFile:
        yield line.split(',')

def main(freqDic, minSup):
    data = read_input(sys.stdin)
    for names in data:
        names = {name:freqDic[int(name)] for name in names \
                 if name.isdigit() \
                 and freqDic.get(int(name), 0) >= minSup}
        lenth = len(names)
        if lenth >= 2:
            conPatItems = [name for name, value in \
                           sorted(names.iteritems(), \
                                  key = lambda p:p[1])]
            for i in range(lenth-1):
                print "%s\t%s" % (conPatItems[i], conPatItems[i+1::])
        else:
            continue

if __name__ == '__main__':
    support = 100
    dic = creatDic()
    main(dic, support)
