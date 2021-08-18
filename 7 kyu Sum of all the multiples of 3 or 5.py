"""
https://www.codewars.com/kata/57f36495c0bb25ecf50000e7/train/python

Your task is to write function findSum.

Upto and including n, this function will return the sum of all multiples of 3 and 5.

For example:

findSum(5) should return 8 (3 + 5)

findSum(10) should return 33 (3 + 5 + 6 + 9 + 10)
"""


def find(n):
    # first:
#     total = 0
    
#     for i in range(n+1):
#         if i % 3 == 0:
#             total += i
#         elif i % 5 == 0:
#             total += i
            
#     return total

    # second:
    return sum([i for i in range(n+1) if i % 3 == 0 or i % 5 == 0])
