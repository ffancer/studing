"""
https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""


# mine:
def find_short(s):
    s = s.split()
    l = 100  # "min_len" is better but autor choose 'l'
    
    for i in s:
        if l > len(i):
            l = len(i)
            
    return l # l: shortest word length
  
  
  # the best someone else's solution in my opinion:
  def find_short(s):
    return min(len(x) for x in s.split())
  
