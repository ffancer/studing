"""
https://www.codewars.com/kata/576b93db1129fcf2200001e6/train/python

Example:

{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6


If array is empty, null or None, or if only 1 Element exists, return 0.
Note:In C++ instead null an empty vector is used. In C there is no null. ;-)

-- There's no null in Haskell, therefore Maybe [Int] is used. Nothing represents null.

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.
"""


def sum_array(arr):
    if arr == [] or arr == None or len(arr) == 1:
        return 0
    
    arr.remove(max(arr))
    arr.remove(min(arr))
    
    return sum(arr)
