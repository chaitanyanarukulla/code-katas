"""Kata: Sort By Binary Ones -  implement a function that sort a 
list of integers based on it's binary representation.

#1 Best Practices Solution by biskinis & others

def sortByBinaryOnes(numList):
    def key(n):
        s = format(n, 'b')
        return -s.count('1'), len(s), n
    return sorted(numList, key=key)"""


def sortByBinaryOnes(numList): 
    """my solution with the help of stack overflow""" 
    return sorted(numList, key=lambda n: (-bin(n).count('1'), len(bin(n)), n))