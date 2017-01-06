collatz_cache = [None for i in range(1000000)]
collatz_cache[0] = 0
collatz_cache[1] = 1


def compute_collatz_chain(n):
    if n < len(collatz_cache):
        if collatz_cache[n] is not None:
            return collatz_cache[n]

        if n == 1:
            return 1
        elif n % 2 == 0:
            collatz_cache[n] = compute_collatz_chain(n // 2) + 1
        else:
            collatz_cache[n] = compute_collatz_chain(3 * n + 1) + 1
        return collatz_cache[n]
    else:

        if n % 2 == 0:
            return compute_collatz_chain(n // 2) + 1
        else:
            return compute_collatz_chain(3 * n + 1) + 1


for i in range(2, 1000000):
    compute_collatz_chain(i)

print(max([i for i in enumerate(collatz_cache)], key=lambda x: x[1]))
