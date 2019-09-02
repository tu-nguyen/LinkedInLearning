#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'This is a long string with a bunch of words in it.'
# print(s.split()) # splits the string into a list
# print(s.split('i'))  # splits on the letter i
l = s.split()
s2 = ":".join(l)  # returns This:is:a:long:string:with:a:bunch:of:words:in:it.
print(s2)
