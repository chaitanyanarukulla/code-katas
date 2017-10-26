"""Kata: Sum of the first nth term of Series

#1 Best Practices Solution by :
doctornick5, Slx64, ninja37, FablehavenGeek, nabrarpour4
(plus 18 more warriors)

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
"""


def series_sum(n):
    """This function outputs total sum of the nth term of a series"""
    if n == 0:
        sum = 0
    else:
        sum = 1
        for i in range(1, n):
            sum += 1.00 / (3 * i + 1)
    total = "%.2f" % sum
    return total
