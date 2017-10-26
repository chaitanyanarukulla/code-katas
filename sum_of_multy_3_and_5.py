"""Kata: Multiples of 3 and 5 - Return the Sum of Multiples of 3 and 5

#1 Best Practices Solution by CrazyMerlyn & others

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

"""


def solution(number):
    """Gets all numbers which are multiples of 5 or 3 and sums up"""
    sum_of_thr_fiv = 0
    for i in range(number):
        if i % 5 == 0 or i % 3 == 0:
            sum_of_thr_fiv = sum_of_thr_fiv + i
    return sum_of_thr_fiv
