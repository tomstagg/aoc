""" Day 10: Cathode-Ray Tube """

signals = [s.split(" ") for s in open("./resources/10_test.txt").read().splitlines()]
# signals = [["noop"], ["addx", "3"], ["addx", "-5"], ["noop"]]
# signals = [["noop"], ["noop"],["noop"], ["addx", "1"], ["addx", "1"],["addx","1"], ["noop"]]
# print(signals)

cycle = 1
addx = None
i = 0
x = 1

results = []
x_inc = 0
crt = 0

while True and len(signals) > i:
    x += x_inc 
    initial = signals[i]
    # print(cycle, x, True if x <= crt + 1 and x >= crt - 1 else False, initial)
    crt += 1
    results.append(x * cycle)

    if signals[i][0] == "noop":
        i += 1
        x_inc = 0 
    elif signals[i][0] == "addx":
        if addx is None:
            addx = cycle + 1
            x_inc = 0
        if cycle == addx:
            x_inc = int(signals[i][1])
            i += 1
            addx = None
    cycle +=1



    # print(f"{cycle-1}-{cycle}", x, x_inc, initial, addx)

for i in range(60):
    print(i)
# print(results)

# print([x for i, x in enumerate(range(230)) if (i-19) % 40 == 0])
# print("part1:", sum([x for i, x in enumerate(results) if (i-19) % 40 == 0]))
# print("part1:", sum([x for i, x in enumerate(results) if (i-19) % 40 == 0]))

