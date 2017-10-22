"""Kata: Nickname Generator - RWrite a function, nicknameGenerator
that takes a string name as an argument and returns 
the first 3 or 4 letters as a nickname..

#1 Best Practices Solution by Blind4Basics & others

def nickname_generator(name):
    return "Error: Name too short" if len(name) < 4 else name[:3+(name[2] in "aeiuo")]
"""

def nickname_generator(name):
    if len(name) < 4:
        return "Error: Name too short"
    if name[2] in ["a","e","i","o","u"]:
        return name[:4]
    else:
        return name[:3]