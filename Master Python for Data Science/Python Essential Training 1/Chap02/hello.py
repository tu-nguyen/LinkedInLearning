#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42

print('Hello, World. {}'.format(x))

print('Hello, World. %d' % x) # legacy code, reminds me of C

print(f'Hello, World. {x}') # f string

# format is a method OF the string