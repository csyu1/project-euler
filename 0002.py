fib_cache = [1, 1]


def fib(n):
    if n >= len(fib_cache):
        ans = fib(n - 1) + fib(n - 2)
        fib_cache.append(ans)
    return fib_cache[n]


while(max(fib_cache) < 4000000):
    fib(len(fib_cache))


print(sum(x for x in fib_cache if x % 2 == 0))
