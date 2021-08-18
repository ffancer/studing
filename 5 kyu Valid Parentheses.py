"""
https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python

Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
Examples

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints

0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""


def valid_parentheses(string):
    cnt = 0

    for i in string:
        if i == '(':
            cnt += 1
        if i == ')':
            cnt -= 1
        if cnt < 0:
            return False

    return cnt == 0
  
  
print(valid_parentheses("  ("))
print(valid_parentheses(")test"))
print(valid_parentheses(""))
print(valid_parentheses("hi())("))
print(valid_parentheses("hi(hi)()"))
