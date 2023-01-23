import string



def scorer(item):
    return string.ascii_letters.index(item) + 1


def part_1(data):
    result = 0
    for item in data:
        first, second = item[:len(item)//2], item[len(item)//2:]
        common_item = (set(first) & set(second)).pop()
        result += scorer(common_item)
    print (result)


def part_2(data):
    result = 0
    group = []

    for i in range(0, len(data),3):
        rucsac_1,rucsac_2, rucsac_3 = data[i:i+3]
        commmon_item = (set(rucsac_1) & set(rucsac_2) & set(rucsac_3)).pop()
        result += scorer(commmon_item)
    print(result)


data = [i.strip() for i in open('input.txt')]

part_1(data) # 7889
part_2(data) # 2825



# Notes
# use range to get list of three items and unpack
# use ascii_letters for all list of lower and upper case chars
item = (set('abc') & set('cde'))
a, = item  # unpacking only the first and only item using tuple unpacking



