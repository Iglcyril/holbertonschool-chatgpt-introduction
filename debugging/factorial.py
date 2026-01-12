#!/usr/bin/python3
import sys
# In this exercise, the function "n -= 1" was missing on line 8 after "result *= n".
# Without this line, it creates an infinite loop, because the loop isn't given an iteration to calculate the the factorial.

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

f = factorial(int(sys.argv[1]))
print(f)