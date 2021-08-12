"""
https://www.codewars.com/kata/58df8b4d010a9456140000c7/solutions

A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of numerical palindromes are:

2332
110011
54322345

For a given number num, return its closest numerical palindrome which can either be smaller or larger than num. If there are 2 possible values, the larger value should be returned. If num is a numerical palindrome itself, return it.

For this kata, single digit numbers will NOT be considered numerical palindromes.

Also, you know the drill - be sure to return "Not valid" if the input is not an integer or is less than 0.

palindrome(8) => 11
palindrome(281) => 282 
palindrome(1029) => 1001
palindrome(1221) => 1221
palindrome("1221") => "Not valid"

In Haskell the function should return a Maybe Int with Nothing for cases where the argument is less than zero.
"""


#                                              THIS SOLUTION DIDNT WORK in 15% of digits


def palindrome(num): 
    if type(num) == str or num < 0:
        return "Not valid"
    
    if 9 >= num >= 0:
        return 11
    
    num = list(str(num))
    
    if len(num) == 3:
        return int(''.join(num[:2] + list(num[0])))
        
    half_of_palindrome = num[:len(num)//2]

    return int(''.join(half_of_palindrome + half_of_palindrome[::-1]))


