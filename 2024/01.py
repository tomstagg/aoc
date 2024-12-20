""" Day 01:Historian Hysteria """

data = open('./resources/01_test.txt').read().splitlines()

loc_1, loc_2 = [], []

loc_1 = [ int(item.split('   ')[0]) for item in data]
loc_2 = [ int(item.split('   ')[1]) for item in data]

part_1 = sum([abs(b-a) for a,b in zip(sorted(loc_1), sorted(loc_2))])

occurance = {}

for item in loc_2:
    if item in occurance:
        occurance[item] += 1
    else:
        occurance[item] = 1

part_2 = sum(item * occurance.get(item, 0) for item in loc_1)


print(part_1, part_2) #2_264_607, 19_457_120


data = [*map(int, open('./resources/01_test.txt').read().split())]
print(data[0::2], data)
# A, B = sorted(data[0::2]), sorted(data[1::2])
# print(sum(map(lambda a, b: abs(a-b), A, B)),
#       sum(map(lambda a: a * B.count(a), A)))