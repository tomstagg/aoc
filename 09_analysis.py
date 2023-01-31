data = open("./resources/09_input.txt").read().splitlines()

rope = [[0, 0] for _ in range(10)]
visits = [set() for _ in rope]


def printout():
    for y in range(-20, 1):
        for x in range(0, 10):
            render = "."
            for idx, val in enumerate(rope):
                if x == val[0] and y == val[1]:
                    render = "H" if idx == 0 else idx
                    break
            print(render, end=" ")
        print()
    print(rope)
    print()


move = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}

nudge = lambda x: 1 if x > 0 else (-1 if x < 0 else 0)
print("== INITIAL STATE ==")
# printout()
for cmd in data:
    direction, steps = cmd.split(" ")
    # print("== ", direction, steps, " ==")
    for _ in range(int(steps)):
        dx, dy = move[direction]
        rope[0][0] += dx
        rope[0][1] += dy

        for i in range(1, len(rope)):
            h_x, h_y = rope[i - 1]
            t_x, t_y = rope[i]

            dx = h_x - t_x
            dy = h_y - t_y

            # if dx == 0 or dy == 0:
            #     t_x += nudge(dx)
            #     t_y += nudge(dy)
            # elif (abs(dx), abs(dy)) != (1,1):
            #     t_x += nudge(dx)
            #     t_y += nudge(dy)


            # moves laterally or vertically away from diagonally
            if (abs(dx) > 1 and abs(dy) == 1) or (abs(dy) > 1 and abs(dx) == 1):
                t_x += nudge(dx)
                t_y += nudge(dy)
            # moves diagonally away by 2 - part 2 pattern only
            if abs(dx) > 1 and abs(dy) > 1:
                t_x += nudge(dx)
                t_y += nudge(dy)
            # moves lateral or vertical away by 2
            if (abs(dx) > 1 and dy == 0) or (abs(dy) > 1 and dx == 0):
                t_x += nudge(dx)
                t_y += nudge(dy)

            rope[i] = [t_x, t_y]

            visits[i].add(",".join([str(x) for x in rope[i]]))
        # printout()

print("part1:", len(visits[1]), "part2:", len(visits[9])) # p1: 6406, p2: 2643