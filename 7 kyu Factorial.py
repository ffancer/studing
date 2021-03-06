"""
https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python

In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) or 
IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) or ValueError (Python) or return -1 (C).
"""


from math import factorial as fac


def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif 2 <= n < 13:
        return fac(n)
    else:
        raise ValueError('Value Error')


print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(-1))
print(factorial(25))
