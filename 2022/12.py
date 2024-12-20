""" Day 12/2022: Hill Climbing Algorithm """

import random
import string
import math

data = open("./resources/12_test.txt").read().splitlines()
# data = open("./resources/12_input.txt").read().splitlines()

h_map = []


start = ()
for y, row in enumerate(data):
    h_map.append(list(row))
    for x, item in enumerate(row):
        if item == "S":
            start = (x, y)
            # path.append((x, y))

x_max = len(h_map[0])
y_max = len(h_map)


# print(h_map)

value = lambda x: list("SabcdefghijklmnopqrstuvwxyzE").index(x) + 1
get_height = lambda x, y: value(h_map[y][x])


curr_h = 1
dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]

min_count = 10000


# for attempt in range (100):
#     count = 0
#     path = []
#     path.append(start)
#     curr_h = 1
#     for i in range(100):
#         new_h = "-"
#         loc = path[-1]
#         step = random.choice(dir)
#         x_new, y_new = loc[0]+ step[0], loc[1] + step[1]

#         if x_new >= 0 and x_new < x_max and (y_new >= 0 and y_new < y_max):
#             new_h = value(h_map[y_new][x_new])
#             if new_h - curr_h == 0 or new_h - curr_h == 1:
#                 curr_h = new_h
#                 path.append((x_new, y_new))
#                 # print((x_new, y_new), h_map[y_new][x_new], new_h, curr_h)
#                 count += 1

#     min_count = count if count < min_count else min_count
#     print(attempt, count, min_count, new_h)

path = []
path.append(start)

def find_optimal_path(scan_steps):
    optimum_path = []
    optimum_count = math.inf
    for scan in range(10):
        scan_path = []
        curr_x, curr_y = path[-1]
        curr_h = get_height(curr_x, curr_y)
        scan_h = curr_h
        while curr_h + scan_steps > scan_h:
            ran_x, ran_y = random.choice(dir)
            search_x, search_y = curr_x + ran_x, curr_y + ran_y
            # print(search_x, search_y, curr_h, scan_path)

            if search_x >= 0 and search_x < x_max and search_y >= 0 and search_y < y_max:
                search_h = get_height(search_x, search_y)
                if search_h - scan_h in [0, 1]:
                    scan_path.append(((search_x, search_y), search_h))
                    scan_h = search_h
                    curr_x, curr_y = search_x, search_y
        # print(scan_path, len(scan_path))
        if len(scan_path) < optimum_count:
            optimum_count = len(scan_path)
            optimum_path = [p[0] for p in scan_path if p[1] - curr_h < scan_steps]
    # print("******", optimum_path, optimum_count, curr_h)

    return optimum_path
    # print((x_new, y_new), h_map[y_new][x_new], new_h, curr_h)

for x in range(5):
    print(path)
    path.extend(find_optimal_path(3))

print(path)
# path.extend(find_optimal_path(3))
# path.extend(find_optimal_path(3))
# path.extend(find_optimal_path(3))




# find_optimal_path(3)

# y = [((0, 1), 2), ((1, 1), 3), ((1, 2), 4)]
# print(y)
# print([x for x in y if x[1] - curr_h < 3])

# print(path, curr_h)

# repeat unti optimal path is found:
# at location find path to curr_h + 2,
# use random steps and write each path to search_path
# overwrite search_path if a shorter route is found
# then write this search_path from curr_h to curr_h + 1
# increment curr_h
# update curr_h+1
# then move to height +1

# print(h_map[5][4])


# def print_map():
#     for y in range(y_max):
#         for x in range(x_max):
#             token = '.' if (x,y) not in path else 'X'
#             print(token, end='')
#         print()
#     print("height:", heights[curr_h])
#     print(path)


# print_map()
