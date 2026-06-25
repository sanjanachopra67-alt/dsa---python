# Given a positive integer n, find the factorial of n using recursion.

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)