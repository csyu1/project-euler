with open('triangle67.txt', 'r') as file:
    pyramid_text = file.read()

pyramid = pyramid_text.split('\n')
for i, row in enumerate(pyramid):
    pyramid[i] = list(map(int, row.split(' ')))


path_costs = []
for idx, row in enumerate(pyramid):
    path_costs.append([None for i in range(idx + 1)])

path_costs[0][0] = pyramid[0][0]


def max_path(pyramid, j, k):

    if path_costs[j][k] is not None:
        return path_costs[j][k]

    try:
        if 0 <= j - 1:
            left_path_cost = max_path(pyramid, j - 1, k)
        else:
            raise IndexError
    except IndexError:
        left_path_cost = 0

    try:
        if 0 <= j - 1 and 0 <= k - 1:
            right_path_cost = max_path(pyramid, j - 1, k - 1)
        else:
            raise IndexError
    except IndexError:
        right_path_cost = 0

    path_costs[j][k] = pyramid[j][k] + max(left_path_cost, right_path_cost)
    return path_costs[j][k]


for idx, node in enumerate(pyramid[-1]):
    max_path(pyramid, len(pyramid) - 1, idx)

print(max(path_costs[-1]))
