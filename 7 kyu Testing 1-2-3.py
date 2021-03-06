"""
https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python

Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples:

number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
"""


def number(lines):
    # first:
#     lst = []
    
#     for i in range(len(lines)):
#         lst.append(f'{i+1}: {lines[i]}')
        
#     return lst

    #second:
#     return [f'{i+1}: {lines[i]}' for i in range(len(lines))]

    # third:
    return [f'{i+1}: {j}' for i,j in enumerate(lines)]
