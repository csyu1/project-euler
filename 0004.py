from itertools import product
from utils import is_palindrome
three_digits = range(100, 1000)

"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

print(max((i * j, i, j)
      for i, j in list(product(three_digits, three_digits))
      if is_palindrome(i * j)))
