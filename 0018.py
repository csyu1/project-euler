pyramid_text = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

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
