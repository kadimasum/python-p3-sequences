#!/usr/bin/env python3

def print_fibonacci(length):
    n1, n2 = 0,1
    count = 0
    result = []

    if length == 0: 
        print(result)
    if length == 1:
        print(n1)
    else:
        while count < length:
            result.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
    print(result)
    