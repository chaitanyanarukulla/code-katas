"""Kata: Sum a list but ignore any duplicates.

#1 Best Practices Solution by anter69 & others

def sum_no_duplicates(l):
    return sum(n for n in set(l) if l.count(n) == 1)"""

from collections import Counter
def sum_no_duplicates(l):
  return sum(value for value, count in Counter(l).items() if count == 1)

