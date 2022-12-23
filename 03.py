with open ('test.txt') as  f:
    data = f.read().splitlines()


def split_rucksac(items: str):
    mid = int(len(items)/2)

    return items[:mid], items[mid:]

print(data)


for contents in data:
    first, second = split_rucksac(contents)
    print(set(first) & set(second))


def score(char):
    

print(ord('a'), ord('b'), ord('A'), ord('B'))
