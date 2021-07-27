"""
https://www.codewars.com/kata/598f76a44f613e0e0b000026/train/python

Your task in this kata is to implement a function that calculates the sum of the integers inside a string. 
For example, in the string "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", the sum of the integers is 3635.

Note: only positive integers will be tested.
"""


def sum_of_integers_in_string(s):
    total, num = 0, ''
    for i in s:
        if i.isdigit():
            num += i
        elif num != '':
            total += int(num)
            num = ''
    if num != '':
        total += int(num)
    return total
  

print(sum_of_integers_in_string('The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog'))
