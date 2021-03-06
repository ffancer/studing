"""
https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
Examples

[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""


def find_outlier(integers):
    integers = list(set(integers))  
    even_or_odd = 0  

    for i in integers:
        if i % 2 == 0:
            even_or_odd += 1
        else:
            even_or_odd -= 1

    if even_or_odd > -1:
        for i in integers:
            if i % 2 != 0:
                return i
    else:
        for i in integers:
            if i % 2 == 0:
                return i
            
  # more better and fast:

#  def find_outlier(integers):
#     integers = list(set(integers))
#     lst_even = []
#     lst_odd = []

#     for i in integers:
#         if i % 2 == 0:
#             lst_even.append(i)
#         else:
#             lst_odd.append(i)

#     if len(lst_even) == 1:
#         return lst_even[0]
#     return lst_odd[0]
