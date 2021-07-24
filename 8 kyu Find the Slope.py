"""
https://www.codewars.com/

Given an array of 4 integers
[a,b,c,d] representing two points (a, b) and (c, d), return a string representation of the slope of the line joining these two points.

For an undefined slope (division by 0), return undefined . Note that the "undefined" is case-sensitive.

   a:x1
   b:y1
   c:x2
   d:y2

Assume that [a,b,c,d] and the answer are all integers (no floating numbers!). Slope: https://en.wikipedia.org/wiki/Slope
"""


def find_slope(points):
    while True:
        try:
            m = (points[3] - points[1]) // (points[2] - points[0])
        except ZeroDivisionError:
            return 'undefined'
        else:
            return str(m
            
            
print(find_slope([19,3,20,3]),"0")
print(find_slope([-7,2,-7,4]),"undefined")
print(find_slope([10,50,30,150]),"5")
print(find_slope([10,20,20,80]),"6")
print(find_slope([-10,6,-10,3]),"undefined")   
