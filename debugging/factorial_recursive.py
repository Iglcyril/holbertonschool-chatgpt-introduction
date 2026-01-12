#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.
    
    The factorial of a number n (denoted n!) is the product of all positive 
    integers less than or equal to n. For example: 5! = 5 × 4 × 3 × 2 × 1 = 120
    This function uses a recursive approach where factorial(n) = n × factorial(n-1).
    
    Parameters:
    n (int): A non-negative integer for which to calculate the factorial.
             Must be >= 0.
    
    Returns:
    int: The factorial of n. Returns 1 if n is 0 (by definition, 0! = 1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the number from command line argument and convert to integer
f = factorial(int(sys.argv[1]))
# Print the result
print(f)