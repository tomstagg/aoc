"""Day 04: Ceres Seach """

d = [list(line) for line in open("./resources/04.txt").read().splitlines()]
xmas = list("XMAS")

moves = [0,1,-1]
move_combos = [(x,y) for x in moves for y in moves]
offset_i, offset_j = 0, 0
max_i, max_j = len(d[:][0]), len(d[0])

result_1 =0
for i in range(max_i):
    for j in range(max_j):
        # print(i,j)
        for search in move_combos:
            offset_i, offset_j = 0, 0
            for pos in range(4):
                i_scan, j_scan = i + offset_i, j + offset_j
                if i_scan < 0 or j_scan < 0 or i_scan == max_i or j_scan == max_j:
                    break
                if d[i + offset_i][j + offset_j] == xmas[pos]:
                    print(i, j, i + offset_i, j + offset_j, d[i+offset_i][j + offset_j], xmas[pos], search)
                    offset_j += search[1] 
                    offset_i += search[0]
                    if xmas[pos] == "S":
                        result_1 += 1
                else:
                    break          

print(result_1)
