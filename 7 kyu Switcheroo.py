"""
https://www.codewars.com/kata/57f759bb664021a30300007d/train/python

Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

Example:

'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb'
"""


def switcheroo(s):
    answer = ''
    
    for i in s:
        if i == 'a':
            answer += 'b'
        elif i == 'b':
            answer += 'a'
        else:
            answer += i
            
    return answer
