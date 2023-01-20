#!/usr/bin/env python3
"""Day 8: Treetop Tree House"""

data = open("./resources/08_test.txt").read()
trees = []

for line in data.split():
    trees.append([int(i) for i in list(line)])

up = lambda x, y: [t[y] for t in trees[x + 1 :]]
down = lambda x, y: [t[y] for t in trees[:x]]
left = lambda x, y: trees[x][y + 1 :]
right = lambda x, y: trees[x][:y]
visible = lambda i, j, direction: trees[i][j] > max(direction(i, j), default=-1)

counter = 0


for i in range(len(trees)):
    for j in range(len(trees[0])):
        if visible(i, j, up) or visible(i, j, down) or visible(i, j, left) or visible(i, j, right):
            counter += 1
        print(i, j, trees[i][j], visible(i, j, up))


print("part 1:", counter)



# Tests
# x, y = 4, 0
# print("down", trees[x][y], down(x, y), visible(x, y, down))
# print("up", trees[x][y], up(x, y), visible(x, y, up))
# print("left", trees[x][y], left(x, y), visible(x, y, left))
# print("right", trees[x][y], right(x, y), visible(x, y, right))
