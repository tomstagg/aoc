""" Day 07/2022: No Space Left On Device """

"""Using a dict approach"""

from collections import defaultdict


dirs = defaultdict(int)
path = []

lines = map(str.split, open("./resources/07_test.txt").read().splitlines())


for l in lines:
    if l[0] == "$":
        if l[1] == "cd":
            if l[2] == "..":
                path.pop()
            else:
                path.append(l[2])
    elif l[0] != "dir":
        for i in range(len(path)):
            dirs[tuple(path[: i + 1])] += int(l[0])
    print(l)
    print(dirs)
    print(path)
    print('*' * 5)


# path_test = ["a", "b", "c"]

# for i in range(len(path_test)):
#     print(tuple(path_test[: i + 1]))
#     # dirs[tuple(path_test[: i + 1])] += int(1)

# for v in dirs.values():
#     print(v)



print("part 1", sum([v for v in dirs.values() if v <=100000]))
print("part 2", min([v for v in dirs.values() if v >= max(dirs.values()) - 40000000 ]))

# print(path_test)
# print(len(path_test))
# print(range(len(path_test)))
# print(tuple(path_test))

# print(dirs)

# /
#     a
#         e
#             i 584
#         f 29116
#         g 2557
#         h 62596
#     b 14848514
#     c 8504156
#     d
#         j 8033020
#         d.log 8033020
#         d.ext 5626152
#         k 7214296
