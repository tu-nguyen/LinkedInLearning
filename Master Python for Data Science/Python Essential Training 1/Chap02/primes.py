#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


def list_primes():
    for n in range(100):
        if isprime(n):
            print(n, end=" ", flush=True)
        print()


# n = 5
# if isprime(n):
#     print(f'{n} is prime')
# else:
#     print(f'{n} not prime')

list_primes()
