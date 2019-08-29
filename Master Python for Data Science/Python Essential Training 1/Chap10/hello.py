#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys


def main():
    # print('Hello, World.')
    try:
        # x = int("foo")
        x = 5 / 0
    except ValueError:  # executes if try fails
        print("I caught a ValueError")
        # captures the error and code will continue
    # ValueError: invalid literal for int() with base 10: 'foo'
    # except ZeroDivisionError:
    #     print("don't divide by zero")
    except:
        print(f"unknown error: {sys.exc_info()}")
    else:  # only executes if you don't have an error
        print("good job!")


if __name__ == '__main__':
    main()
