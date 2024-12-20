#!/usr/bin/env python3

""" 2022/06: Tuning Trouble"""


data_streams = open('resources/06_test.txt').read().strip().splitlines()


def process(d):
    result = ()
    for ds in data_streams:
        for i in range(d, len(ds)):
            if len(set(ds[i-d:i])) == d:
                result = (*result, i)
                break
    return result


alt = lambda N: next(i for i in range(N, len(ds)) if len(set(ds[i-N:i]))==N)


print("part 1:", process(4))
print("part 2:", process(14))


ds = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"



print("part 1:", alt(4))