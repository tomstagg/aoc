"""Day 02: Red-Nosed Reports"""

data = open("./resources/02.txt").read().splitlines()

count_1, count_2 = 0, 0

# this will check if the levels are decreasing or increasing within tolerance
verify_dec = lambda report: [(a-b) > 0 and abs(a-b) < 4 for a,b in zip(report, report[1:])]
verify_inc = lambda report: [(a-b) < 0 and abs(a-b) < 4 for a,b in zip(report, report[1:])]

for item in data[:]:
    report = [*map(int,item.split())]
    dec = verify_dec(report)
    inc = verify_inc(report)

    # validate if all checks are True in either result
    if (all(inc) or all(dec)):
        count_1 += 1
        count_2 += 1
    else:
        # iterate over each report and remove one level at a time and check if valid
        for i in range(len(report)):
            correct_report = list(report)
            del correct_report[i]
            dec = verify_dec(correct_report)
            inc = verify_inc(correct_report)

            if (all(inc) or all(dec)):
                count_2 += 1
                break
        
print(count_1, count_2)

# another way #1
def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    return set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}

data = [[int(y) for y in x.split(' ')] for x in open('resources/02.txt').read().split('\n')]

safe_count = sum([is_safe(row) for row in data])
print(safe_count)

safe_count = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in data])
print(safe_count)

# another way #2
data = [[*map(int, l.split())] for l in open('resources/02.txt')]

def good(d, s=0):
    for i in range(len(d)-1):
        if not 1 <= d[i]-d[i+1] <= 3:
            return s and any(good(d[j-1:j] + d[j+1:]) for j in (i,i+1))
    return True

for s in 0, 1: 
    print(sum(good(d, s) or good(d[::-1], s) for d in data))


# to compare adajent item can just use d[i], d[i+1]
# reverse a list so don't need inc and dec options using d[::-1]
# set reduces all values down to unique values