import math


def is_prime(n):
    if n < 2:
        return False
    if n <= 3:
        return True
    for i in range(2, int(math.ceil(math.sqrt(n))) + 1):
        if n % i == 0:
            return False
    return True


assert(is_prime(2) is True)
assert(is_prime(3) is True)
assert(is_prime(4) is False)
assert(is_prime(5) is True)
assert(is_prime(6) is False)
assert(is_prime(7) is True)
assert(is_prime(8) is False)
assert(is_prime(9) is False)
assert(is_prime(10) is False)
assert(is_prime(11) is True)
assert(is_prime(97))
assert(not is_prime(99))


def is_palindrome(x):
    if not isinstance(x, str):
        x = str(x)
    return x == x[::-1]


assert(is_palindrome(1))
assert(is_palindrome(11))
assert(not is_palindrome(12))
assert(is_palindrome("testset"))
assert(not is_palindrome("5 testset"))


def sieve(n):
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    # True is prime
    sieve_integers = [True if i > 1 else False for i in range(n + 1)]
    for idx, p in enumerate(sieve_integers):
        if not p:
            continue
        to_mark = idx + idx
        while to_mark <= n:
            sieve_integers[to_mark] = False
            to_mark += idx
    numbers = [i for i, prime_check
               in enumerate(sieve_integers)
               if prime_check]
    return numbers
assert(sieve(5) == [2, 3, 5])
assert(sieve(10) == [2, 3, 5, 7])
assert(sieve(20) == [2, 3, 5, 7, 11, 13, 17, 19])
