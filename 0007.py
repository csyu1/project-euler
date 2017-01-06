"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

target = 10001

primes = [2, 3, 5, 7, 11, 13]
candidate = max(primes) + 2
while len(primes) < target:
    if all(map(lambda x: candidate % x != 0, primes)):
        primes.append(candidate)
    candidate += 2
print(primes[10000])
