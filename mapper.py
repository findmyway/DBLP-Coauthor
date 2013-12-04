#!/usr/bin/env python
import sys
def read_input(file):
    for line in file:
        yield line.split(',')

def main():
    data = read_input(sys.stdin)
    for names in data:
        for name in names:
            if name.isdigit():
                print '%s\t%d' % (name, 1)
if __name__ == "__main__":
    main()
