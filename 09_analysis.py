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
    print("== ", direction, steps, " ==")
    for _ in range(int(steps)):
        dx, dy = move[direction]
        rope[0][0] += dx
        rope[0][1] += dy

        for i in range(1, len(rope)):
            h_x, h_y = rope[i - 1]
            t_x, t_y = rope[i]

            dx = h_x - t_x
            dy = h_y - t_y

            if dx == 0 or dy == 0:
                if abs(dx) == 2:
                    t_x += nudge(dx)
                if abs(dy) == 2:
                    t_y += nudge(dy)
            elif (abs(dx), abs(dy)) != (1,1):
                t_x += nudge(dx)
                t_y += nudge(dy)

            rope[i] = [t_x, t_y]

            visits[i].add(",".join([str(x) for x in rope[i]]))
        # printout()

print("part1:", len(visits[1]), "part2:", len(visits[9])) # p1: 6406, p2: 2643




# complex number solution - probably the best

# rope = [0] * 10
# seen = [set([x]) for x in rope]
# dirs = {'L':+1, 'R':-1, 'D':1j, 'U':-1j}
# sign = lambda x: complex((x.real>0) - (x.real<0), (x.imag>0) - (x.imag<0))

# for line in open('in.txt'):
#     for _ in range(int(line[2:])):
#         rope[0] += dirs[line[0]]

#         for i in range(1, 10):
#             dist = rope[i-1] - rope[i]
#             if abs(dist) >= 2:
#                 rope[i] += sign(dist)
#                 seen[i].add(rope[i])

# print(len(seen[1]), len(seen[9]))