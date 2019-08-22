#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import *

# a = 8
# b = 9

# a = Decimal('.10')
# b = Decimal(".30")
# x = .1 + .1 + .1 - .3 returns 5.551115123125793e-17
# x = a + a + a - b returns correct value of 0.00
x = 1
print('x is {}'.format(x))
print(type(x))

if x:
    print("True")
else:
    print("False")
