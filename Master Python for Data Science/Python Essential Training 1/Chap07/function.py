#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# def main():
#     kitten(3)

# def kitten(n):
#     print(f'{n} Meow.')

# def main():
#     x = kitten()
#     print(x)

# def kitten():
#     return 'Meow.'

# all function returns a value, if none is stated, it returns None
   
def main():
 
    x = 5
    print(id(x))
    kitten(x)
    print(f"In main x is {x}")

def kitten(a):
    print(id(a))
    a = 3
    print(id(a))
    print('Meow.')
    print(a)

if __name__ == '__main__': main()
