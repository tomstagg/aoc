""" Day 10: Cathode-Ray Tube """

signals = [s.split(" ") for s in open("./resources/10_input.txt").read().splitlines()]

cycle = 1
addx = None
i = 0
x = 1

part1, part2 = [], []
x_inc = 0
crt = 0

while True and len(signals) > i:
    x += x_inc
    initial = signals[i]
    part2.append(True if x <= crt % 40 + 1 and x >= crt % 40 - 1 else False)
    crt += 1
    part1.append(x * cycle)

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
    cycle += 1

print("part1:", sum([x for i, x in enumerate(part1) if (i - 19) % 40 == 0]))
print("part2:")
for idx, pixle in enumerate(part2):
    print("#" if pixle else ".", end="")
    if (idx + 1) % 40 == 0:
        print()
