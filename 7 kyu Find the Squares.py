"""
https://www.codewars.com/kata/60908bc1d5811f0025474291/train/python

Problem

Complete the function that takes an odd integer (0 < n < 1000000) which is the difference between two consecutive perfect squares, and return these squares as a string in the format "bigger-smaller"
Examples

9  -->  "25-16"
5  -->  "9-4"
7  -->  "16-9"
"""


def find_squares(num):
    i = 0
    diff = 0
    
    while diff != num:
        i += 1
        diff = (i + 1) ** 2 - i ** 2
        
    return f"{str((i + 1) ** 2)}-{str(i**2)}"
