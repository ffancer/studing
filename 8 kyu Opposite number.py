"""
https://www.codewars.com/kata/56dec885c54a926dcd001095/train/python

Very simple, given a number, find its opposite.

Examples:

1: -1
14: -14
-34: 34
"""


def opposite(number):
    answer = 0
    
    if number > 0:
        answer = -number
    elif number < 0:
        answer = abs(number)
        
    return answer
