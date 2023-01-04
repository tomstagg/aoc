import re

data = open("input.txt").read().splitlines()


def setup():
    stacks = create_stacks()
    load_stacks(stacks)
    return stacks


def create_stacks():
    stacks = []
    for _ in range(0, len(data[0]), 4):
        stacks.append([])
    return stacks


def load_stacks(stacks):
    for row in data:
        for index, i in enumerate(range(1, len(row) + 1, 4)):
            if re.search("\d", row):
                break
            if row[i] != " ":
                stacks[index].append(row[i])

    for index, stack in enumerate(stacks):
        stacks[index].reverse()
    print(stacks)


def rearrange_9000(stacks):
    for row in data:
        if re.match("move", row):
            containers, from_stack, to_stack = map(int, re.findall("\d+", row))
            # print(row)

            for _ in range(containers):
                container = stacks[from_stack - 1].pop()
                stacks[to_stack - 1].append(container)
            # print(stacks)


def rearrange_9001(stacks):
    for row in data:
        if re.match("move", row):
            containers, from_stack, to_stack = map(int, re.findall("\d+", row))
            print(row)

            multiple = []
            for _ in range(containers):
                multiple.append(stacks[from_stack - 1].pop())

            multiple.reverse()

            print(multiple)

            stacks[to_stack - 1].extend(multiple)
            print(stacks)


def get_top(stacks):
    top_stacks = ""
    for i in range(len(stacks)):
        top_stacks += stacks[i].pop()
    print(top_stacks)


def part_1():
    stacks = setup()
    rearrange_9000(stacks)
    get_top(stacks)


def part_2():
    stacks = setup()
    rearrange_9001(stacks)
    get_top(stacks)


part_1()
part_2()
