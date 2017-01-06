first_100 = range(1, 101)
sum_squares = sum(x * x for x in first_100)
square_sum = sum(first_100) ** 2
print(square_sum - sum_squares)
