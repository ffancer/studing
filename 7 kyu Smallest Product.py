"""
https://www.codewars.com/kata/5b6b128783d648c4c4000129/train/python

Given a non-empty array of non-empty integer arrays, multiply the contents of each nested array and return the smallest total.
Example

input = [
  [1, 5],
  [2],
  [-1, -3]
]

result = 2
"""


def smallest_product(a):
    lst = []
    total = 1
    
    for i in a:
        for j in i:
            total *= j
        lst.append(total)
        total = 1
        
    return min(lst)


