def generate_triangle():
    x = 1
    total = 0
    while True:
        total += x
        yield total
        x += 1


def get_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    return set(divisors)


tri_gen = generate_triangle()
x = next(tri_gen)
divisors = get_divisors(x)
while len(divisors) < 500:
    x = next(tri_gen)
    divisors = get_divisors(x)
print(x)
