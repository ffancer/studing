"""
https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!
Examples

get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
"""


def get_sum(a,b):
    if a == b:
        return a
    
    min_num = min(a, b)
    max_num = max(a, b)
    
    return (max_num - min_num + 1) * (min_num + max_num) / 2


# best answer:

# def get_sum(a,b):
#     return sum(range(min(a, b), max(a, b) + 1))
