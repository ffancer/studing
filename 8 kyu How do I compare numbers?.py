"""
What could be easier than comparing integer numbers? However, 
the given piece of code doesn't recognize some of the special numbers for a reason to be found. Your task is to find the bug and eliminate it.
"""


def what_is(x):
    if x == 42:  # just replace 'is' to '=='
        return 'everything'
    elif x == 42 * 42:  # same replace from 'is' to '=='
        return 'everything squared'
    else:
        return 'nothing'
      
      
      
