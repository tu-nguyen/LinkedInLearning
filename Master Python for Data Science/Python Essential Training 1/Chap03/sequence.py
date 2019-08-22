#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# x = [1, 2, 3, 4, 5] <-- list
# x = {1, 2, 3, 4, 5}  # <-- tuple, not mutable
# x[2] = 42

# x = list(range(5))
# x[2] = 42
# for i in x:
#     print('i is {}'.format(i))

# x = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
# x["three"] = 42
# for k, v in x.items():
#     print('k: {}, v: {}'.format(k, v))

x = (1, "two", 3.0, [4, "four"], 5)
y = [1, "two", 3.0, [4, "four"], 5]
print('x is {}'.format(x))
print(id(x[0]))
print(id(y[0]))

# if x is y:
#     print("yup")
# else:
#     print("nop")

if isinstance(y, tuple):
    print("tuple")
elif isinstance(y, list):
    print("list")
else:
    print("nop")
