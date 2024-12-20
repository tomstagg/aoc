from itertools import accumulate

f = lambda x: int(x) if x[-1].isdigit() else 0
xs = [*map(f, open('./resources/10_input.txt').read().split())]

print(xs)
print(accumulate([1]+xs))
part1, part2 = 0, '\n'
for i, x in enumerate(accumulate([1]+xs), 1):
    part1 += i*x if i%40==20 else 0
    part2 += '#' if (i-1)%40-x in [-1,0,1] else ' '

print(part1, *part2)

