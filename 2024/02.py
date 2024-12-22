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
