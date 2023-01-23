from collections import defaultdict


# lines = open('./resources/07_test.txt').read().splitlines()
lines = map(str.split, open('./resources/07_test.txt').read().splitlines())
dirs = defaultdict(int)
path = []



for l in lines:
    print('>>>', l)
    if l[0] == "$":
        if l[1] == "cd":
            if l[2] == "..":
                path.pop()
                print(path)
            else:
                path.append(l[2])
                print(path)
    elif l[0] != "dir":
        for i in range(len(path)):
            print(tuple(path[: i + 1]), int(l[0]))
            dirs[tuple(path[: i + 1])] += int(l[0])


print(dirs)
