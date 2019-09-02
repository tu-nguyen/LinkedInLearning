#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    f = open('lines.txt')  # default is r for read
    # other option is w, which clears the file, a which appends to end of file
    for line in f:
        print(line.rstrip())


if __name__ == '__main__':
    main()
