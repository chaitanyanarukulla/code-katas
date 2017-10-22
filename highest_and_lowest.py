"""Kata: Highest and Lowest - In this little assignment you are given a 
string of space separated numbers, and have to return the highest and lowest number.

#1 Best Practices Solution by CrazyMerlyn & others

def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
"""


def high_and_low(numbers):
    ord_nums= []
    numbers = numbers.split()
    for i in numbers:
        ord_nums.append(int(i))
    result = str(max(ord_nums)) + " " + str(min(ord_nums))
    return result