"""
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function likes which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"

For 4 or more names, the number in and 2 others simply increases.
"""


def likes(names):
    answer = 'no one likes this'
    
    if names == []:
        return answer
    
    elif len(names) == 1:
        answer = f"{names[0]} likes this"
        
    elif len(names) == 2:
        answer = f"{names[0]} and {names[1]} like this"
        
    elif len(names) == 3:
        answer = f"{names[0]}, {names[1]} and {names[2]} like this"
        
    elif len(names) >= 4:
        answer = f"{names[0]}, {names[1]} and {len(names)-2} others like this"
        
    return answer
