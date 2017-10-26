"""Kata: Exclamation marks series #6 -
Remove n exclamation marks in the sentence from left to right.

#1 Best Practices Solution by MiraliN, RuiCatela, Demon Slayer,
Mr.Child, kevin.du, mkosowsk (plus 186 more warriors)

def remove(s, n):
    return s.replace("!", "", n)
"""


def remove(s, n):
    """This function removes exclamation marks n times from left"""
    return s.replace('!','', n)
