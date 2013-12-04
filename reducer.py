#!/usr/bin/env python
from itertools import groupby
from operator import itemgetter
import sys

def readMapOutput(file):
    for line in file:
        yield line.strip().split('\t')

def main():
    data = readMapOutput(sys.stdin)
    for currentName, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for currentName, count in group)
            print "%s\t%d" % (currentName, total_count)
        except ValueError:
            pass

if __name__ == "__main__":
    main()
