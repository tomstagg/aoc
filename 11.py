#!/usr/bin/env python3
""" Day 11/2022: Monkey in the Middle """

from operator import add, sub, mul
import queue
import re
from math import prod


def initialise():
    mk_items, mks = [], []
    # data = open("./resources/11_test.txt").read().splitlines()
    data = open("./resources/11_input.txt").read().splitlines()

    op_map = {"+": add, "-": sub, "*": mul}
    for idx, line in enumerate(data):
        i = idx // 7
        re_match = re.findall(r"([+\-*\/]|\d+|old$)", line)
        if "Start" in line:
            q = queue.Queue()
            for item in re_match:
                q.put(int(item))
            mk_items.append(q)
        if "Operation" in line:
            op = op_map[re_match[0]]
            val = re_match[1]
        if "Test" in line:
            div_test = int(re_match[0])
        if "If true: " in line:
            true_mk = int(re_match[0])
        if "If false: " in line:
            false_mk = int(re_match[0])
            mks.append((op, val, div_test, (true_mk, false_mk)))
    return (mk_items, mks)


calc_wl = (
    lambda cur_wl, op, val, wl_factor: (op(cur_wl, int(val)) // wl_factor)
    if val != "old"
    else op(cur_wl, cur_wl) // wl_factor
)
send_to = lambda wl, test, routing: routing[0] if wl % test == 0 else routing[1]


def rounds(no, wl_factor, parsed):
    mk_items, mks = parsed
    inspected = [0] * len(mks)

    cycle_length = 1
    for _, _, div, _ in mks:
        cycle_length *= div

    for r in range(1, no + 1):

        for i, q_items in enumerate(mk_items):
            # print(f'## turn {i} ##')
            while not q_items.empty():
                op, val, div_test, route = mks[i]
                item = q_items.get()
                wl = calc_wl(item, op, val, wl_factor)
                mk_items[send_to(wl, div_test, route)].put(wl % cycle_length)
                inspected[i] += 1
        if r in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
            print(f"## after round {r} ##")
            for idx, i in enumerate(inspected):
                print(f"Monkey: {idx} inspected {i}")
            print()


    return prod(sorted(inspected)[-2:])


print("part 1:", rounds(20, 3, initialise()))  # test: 10_605, input: 118_674
print("part 2:", rounds(10000, 1, initialise()))  # test 2_713_310_158, input: 32_333_418_600
