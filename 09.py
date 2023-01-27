# a_set = {'a','b'}


# a_set.add('a')

# print(a_set, len(a_set), sep="\n")

h_x, h_y, t_x, t_y = 1, 3, 1, 3

# gap = lambda h_x, h_y, t_x, t_y: (t_x - h_x, t_y - h_y)


# print(gap(1,2,3,4))

for direction in ["R", "R", "U", "U", "L", "L", "R","D","D","D", "D"]:
    if direction == "R":
        h_x += 1
    if direction == "U":
        h_y += -1
    if direction == "L":
        h_x += -1
    if direction == "D":
        h_y += 1

    if (abs(h_x - t_x) > 1 and abs(h_y - t_y) == 1) or (abs(h_y - t_y) > 1 and abs(h_x - t_x) == 1):
        t_x += int((h_x - t_x) * 0.5) if abs(h_x - t_x) > 1 else h_x - t_x
        t_y += int((h_y - t_y) * 0.5) if abs(h_y - t_y) > 1 else h_y - t_y
    elif abs(h_x - t_x) > 1 or abs(h_y - t_y) > 1:
        t_x += int((h_x - t_x) * 0.5) if h_y == t_y else 0
        t_y += int((h_y - t_y) * 0.5) if h_x == t_x else 0


    print(direction, "h:", h_x, h_y, "t:", t_x, t_y)
