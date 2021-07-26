"""
Switch/Case - Bug Fixing #6

Oh no! Timmy's evalObject function doesn't work. He uses Switch/Cases to evaluate the given properties of an object, can you fix timmy's function?
"""


def eval_object(v):
    result = 0
    if '+' in v.values():
        result = v['a'] + v['b']
    elif '-' in v.values():
        result = v['a'] - v['b']
    elif '/' in v.values():
        result = v['a'] / v['b']
    elif '*' in v.values():
        result = v['a'] * v['b']
    elif '%' in v.values():
        result = v['a'] % v['b']
    elif '**' in v.values():
        result = v['a'] ** v['b']
    return result
  
  
print(eval_object({'a': 1, 'b': 1, 'operation': '+'}), 2, 'Return the evaluated string as a number!')
print(eval_object({'a': 1, 'b': 1, 'operation': '-'}), 0, 'Return the evaluated string as a number!')
print(eval_object({'a': 1, 'b': 1, 'operation': '/'}), 1, 'Return the evaluated string as a number!')
print(eval_object({'a': 1, 'b': 1, 'operation': '*'}), 1, 'Return the evaluated string as a number!')
print(eval_object({'a': 1, 'b': 1, 'operation': '%'}), 0, 'Return the evaluated string as a number!')
print(eval_object({'a': 1, 'b': 1, 'operation': '**'}), 1, 'Return the evaluated string as a number!')


"""
best solution is with just blabla.get(v['operation']:

def eval_object(v):
    return {"+": v['a']+v['b'],
            "-": v['a']-v['b'],
            "/": v['a']/v['b'],
            "*": v['a']*v['b'],
            "%": v['a']%v['b'],
           "**": v['a']**v['b'], }.get(v['operation'])  # here was mistake

"""
