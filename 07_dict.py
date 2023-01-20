""" Day 07/2022: No Space Left On Device """

"""Using a dict approach. This builds a stack as we tranverse down each directory.
When a file is parsed the dict is populated with a tuple of the stack and it's value is increment by the file size.
We move up the stack and add it's tuple as a key and incremental it's value by the file size.

Demonstrates:
- dict approach
- match case statement
- itertools accumulate function """

from collections import defaultdict
from itertools import accumulate


dirs, path = defaultdict(int), []

data = open("./resources/07_input.txt").read().splitlines()

lines = map(str.split, data)

# standard if elif flow:
# for l in lines:
#     if l[0] == "$":
#         if l[1] == "cd":
#             if l[2] == "..":
#                 path.pop()
#             else:
#                 path.append(l[2])
#     elif l[0] != "dir":
#         for p in accumulate(path):
#             dirs[p] += int(l[0])


for line in data:
    match line.split():
        case "$", "cd", "..":
            path.pop()
        case "$", "cd", x:
            path.append(x)
        case "$", "ls":
            continue
        case "dir", _:
            continue
        case size, _:
            for p in accumulate(path):
                dirs[p] += int(size)

print(dirs)
print("part 1", sum([v for v in dirs.values() if v <= 100_000]))
print("part 2", min([v for v in dirs.values() if v >= max(dirs.values()) - 40_000_000]))
# part 1 1778099
# part 2 1623571
