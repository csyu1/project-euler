from utils import is_prime

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


n = 600851475143
divisor = 3

while not is_prime(n):
    while n % divisor == 0:
        # continuously divide by the divisor
        # until no factors of the divisor left
        n = n // divisor
    divisor += 2
print(n)
