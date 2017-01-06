
"""
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


for a in range(1, 1000):
    the_one = False
    for b in range(1, 1000 - 1):
        c = (a * a + b * b) ** 0.5
        if a + b + c == 1000:
            print(a, b, c, a * b * c)
            the_one = True
            break
    if the_one:
        break
