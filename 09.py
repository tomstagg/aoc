
data = open("./resources/09_input.txt").read().splitlines()
visits = set()

rope = [[11, -5] for _ in range(10)]

def printout():
    for y in range(-20, 1):
        for x in range(0, 27):
            render = "."
            for idx, val in enumerate(rope):
                if x == val[0] and y == val[1]:
                    render = "H" if idx == 0 else idx
                    break
            print(render, end=" ")
        print()
    print(rope)
    print()

print("== INITIAL STATE ==")
# printout()
for cmd in data:
    direction, steps = cmd.split(" ")
    print("== ", direction, steps, " ==")
    for _ in range(int(steps)):
        h_x, h_y = rope[0]
        if direction == "R":
            h_x += 1
        if direction == "U":
            h_y += -1
        if direction == "L":
            h_x += -1
        if direction == "D":
            h_y += 1
        rope[0] = [h_x, h_y]

        for i in range(1, len(rope)):
            h_x, h_y = rope[i - 1]
            t_x, t_y = rope[i]

            # moves laterally or verticallly away from diagonally
            if (abs(h_x - t_x) > 1 and abs(h_y - t_y) == 1) or (abs(h_y - t_y) > 1 and abs(h_x - t_x) == 1):
                t_x += int((h_x - t_x) * 0.5) if abs(h_x - t_x) > 1 else h_x - t_x
                t_y += int((h_y - t_y) * 0.5) if abs(h_y - t_y) > 1 else h_y - t_y
            # moves diagonally away by 2 - part 2 pattern only
            if abs(h_x - t_x) > 1 and abs(h_y - t_y) > 1:
                t_x += int((h_x - t_x) * 0.5)
                t_y += int((h_y - t_y) * 0.5)
            # moves lateral or vertical away by 2
            elif abs(h_x - t_x) > 1 or abs(h_y - t_y) > 1:
                t_x += int((h_x - t_x) * 0.5) if h_y == t_y else 0
                t_y += int((h_y - t_y) * 0.5) if h_x == t_x else 0

            rope[i] = [t_x, t_y]

            # print(direction, "h:", h_x, h_y, "t:", t_x, t_y)
            visits.add(",".join([str(x) for x in rope[-1]]))
    # printout()

print("part1:", len(visits))  # 6406


