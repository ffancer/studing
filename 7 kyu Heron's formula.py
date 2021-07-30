"""
https://www.codewars.com/kata/57aa218e72292d98d500240f/train/python

Write function heron which calculates the area of a triangle with sides a, b, and c.

Heron's formula:
s∗(s−a)∗(s−b)∗(s−c)\sqrt{s * (s - a) * (s - b) * (s - c)}s∗(s−a)∗(s−b)∗(s−c)
​

where
s=a+b+c2s = \frac{a + b + c} 2s=2a+b+c​
"""


def heron(a,b,c):
    s = (a+b+c) / 2
    return round((s * (s-a)*(s-b)*(s-c))**0.5, 2)
