"""Kata: love vs friendship - Return sum of letter in word given (a=1,b=2,c=3.....).

#1 Best Practices Solution by CrazyMerlyn & others
def words_to_marks(s):
  return sum(ord(c)-96 for c in s)
"""
def words_to_marks(s):
    """did this in  301 class but inJ.script"""
    return sum(ord(letters) % 96 for letters in s)
