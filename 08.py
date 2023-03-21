#!/usr/bin/env python3
"""Day 8: Treetop Tree House"""
from itertools import takewhile

data = open("./resources/08_input.txt").read()
trees = [[int(i) for i in list(line)] for line in data.split()]


def take_until(val, array):
    result = []
    for i in array:
        result.append(i)
        if i >= val:
            break
    return result


up = lambda x, y: [t[y] for t in trees[x + 1 :]]
down = lambda x, y: [t[y] for t in trees[:x]][::-1]
left = lambda x, y: trees[x][y + 1 :]
right = lambda x, y: trees[x][:y][::-1]
is_visible = lambda i, j, direction: trees[i][j] > max(direction(i, j), default=-1)
view_score = lambda x, y, direction: len(take_until(trees[x][y], direction(x, y)))

counter = 0
view_scores = []

for i in range(len(trees)):
    for j in range(len(trees[0])):
        if is_visible(i, j, up) or is_visible(i, j, down) or is_visible(i, j, left) or is_visible(i, j, right):
            counter += 1
        view_scores.append(
            view_score(i, j, up) * view_score(i, j, down) * view_score(i, j, left) * view_score(i, j, right)
        )


print("part 1:", counter)  # 1695
print("part 2:", max(view_scores)) # 287_040

# Tests
# x, y = 3, 2
# print(trees[x][y])
# print("down", trees[x][y], down(x, y), is_visible(x, y, down))
# print("up", trees[x][y], up(x, y), is_visible(x, y, up))
# print("left", trees[x][y], left(x, y), is_visible(x, y, left))
# print("right", trees[x][y], right(x, y), is_visible(x, y, right))

# print("down_view", trees[x][y], down(x, y), view_score(x, y, down))
# print("up_view", trees[x][y], up(x, y), view_score(x, y, up))
# print("left_view", trees[x][y], left(x, y), view_score(x, y, left))
# print("right_view", trees[x][y], right(x, y), view_score(x, y, right))
