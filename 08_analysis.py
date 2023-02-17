import numpy as np

"""
1. Populate the grid with values and two grids of the same shape, one with zeros and the other with ones.
2. Go through each element and get slice to the right, populate boolean result of value is less than the element
3. use `all` to get result. i.e. FF=F, TT=T, FT=F. And do an in-place bitwise OR (|) used for part1
4. use next and generate to get the score based on the boolean array, Using in-place multipler to set part2 grid
5. rotate the array 90 degree anticlockwise and repeat. The part1 and 2 grids are updates considering the previous results
"""

grid = np.array([list(x.strip()) for x in open("./resources/08_test.txt")], int)
part1 = np.zeros_like(grid)
part2 = np.ones_like(grid)

print(grid)
for _ in range(4):
    for x, y in np.ndindex(grid.shape):
        lower = [t < grid[x, y] for t in grid[x, y + 1 :]]

        part1[x, y] |= all(lower)
        part2[x, y] *= next((i + 1 for i, t in enumerate(lower) if ~t), len(lower))
        # print(grid[x,y], grid[x, y+1: ], lower, part1[x,y],part2[x,y])

    grid, part1, part2 = map(np.rot90, [grid, part1, part2])

print(part1.sum(), part2.max())


# ANALYSIS
# numpy lower improvement
ay = np.array([5, 1, 2, 3, 4, 5, 6, 7])
lower = ay[1:] < 3
print(ay)


# return score based on first occurrence of False - which means the tree is the same height or higher than the candidate.
# index() can return the lowest index in the list
for ay in [[True, False, False, False], [True, True, False, False], [True, True, True, False], [True * 4]]:
    print("next and generator:", ay, next((i + 1 for i, t in enumerate(ay) if not t), len(ay)))
    print("index(0)          :", ay, ay.index(0) + 1 if not all(ay) else len(ay))
    # lower.index(0) + 1 if not all(lower) else len(lower)

x = [False, False, False, False, False]
print("index:", x.index(0))

# rotating an array
ay = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(ay)
print(np.rot90(ay))

# tilde usage - works only with boolean underlying bitwise store. This isn't the case for a list of booleans.
# in that case use not
np_true = np.array([True])
true = True
print("np array:", np_true, ~np_true)
print("var or list :", true, ~true)

# rotating a 2d array without numpy
# [::-1] - reverse order, * - makes each sublist a seperate arg for zip, zip - consumers one item from each arg to make a tuple
ay = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rotate = lambda x: list(zip(*x[::-1]))

print(ay, rotate(ay))
