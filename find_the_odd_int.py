"""Kata: Find the odd int - Return the opposite of the input number.

#1 Best Practices Solution by 
cerealdinner, ynnake, sfr, netpsychosis, VadimPopov, user7514902 (plus 291 more warriors)

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
"""
def find_it(seq):
    """Return the  number which  appers odd amount of times."""
    for number in seq:
        if seq.count(number) % 2 != 0:
            return number