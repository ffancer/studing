"""
https://www.codewars.com/kata/59377c53e66267c8f6000027/train/python

Introduction

There is a war and nobody knows - the alphabet war!
There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.
Task

Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

The left side letters and their power:

 w - 4
 p - 3
 b - 2
 s - 1

The right side letters and their power:

 m - 4
 q - 3
 d - 2
 z - 1

The other letters don't have power and are only victims.
Example

AlphabetWar("z");        //=> Right side wins!
AlphabetWar("zdqmwpbs"); //=> Let's fight again!
AlphabetWar("zzzzs");    //=> Right side wins!
AlphabetWar("wwwwwwz");  //=> Left side wins!
"""


def alphabet_war(fight):
    total = 0

    for i in fight:
        if i == 'w':
            total -= 4
        elif i == 'p':
            total -= 3
        elif i == 'b':
            total -= 2
        elif i == 's':
            total -= 1
        elif i == 'm':
            total += 4
        elif i == 'q':
            total += 3
        elif i == 'd':
            total += 2
        elif i == 'z':
            total += 1

    if total == 0:
        answer = "Let's fight again!"
    if total > 0:
        answer = "Right side wins!"
    if total < 0:
        answer = "Left side wins!"

    return answer


print(alphabet_war("z"), "Right side wins!")
print(alphabet_war("zdqmwpbs"), "Let's fight again!")
print(alphabet_war("wq"), "Left side wins!")
print(alphabet_war("zzzzs"), "Right side wins!")
print(alphabet_war("wwwwww"), "Left side wins!")
