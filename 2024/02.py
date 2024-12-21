"""Day 02: Red-Nosed Reports"""

data = open("./resources/02_test.txt").read().splitlines()

count_1, count_2 = 0, 0

verify_dec = lambda report: [(a-b) > 0 and abs(a-b) < 4 for a,b in zip(report, report[1:])]
verify_inc = lambda report: [(a-b) < 0 and abs(a-b) < 4 for a,b in zip(report, report[1:])]

for item in data:
    report = [*map(int,item.split())]
    dec = verify_dec(report)
    inc = verify_inc(report)

    print(report, inc, dec, inc.count(False), dec.count(False))
    # print(report, inc,dec, len(inc), sum(inc), len(dec), sum(dec))
    if (all(inc) or all(dec)):
        count_1 += 1
        count_2 += 1
        print('safe')
    else:
        if inc.count(False) >= 1:
            corrected_report = list(report)
            index = inc.index(False) # remove first false
            del corrected_report[index]
            print('corrected_inc: ', corrected_report)
            if (all(verify_inc(corrected_report)) or all(verify_dec(corrected_report))):
                count_2 += 1
                print('safe_2')
                break
        if dec.count(False) >= 1:
            corrected_report = list(report)
            index = dec.index(False) # remove first false
            del corrected_report[index]
            print('corrected_dec: ', corrected_report)
            if (all(verify_inc(corrected_report)) or all(verify_dec(corrected_report))):
                count_2 += 1
                print('safe_2')
                break


        
print(count_1, count_2)
#     item = [-1,-2,-3,-4,-5]
#     print([(i < 0 or i> 0) and abs(i) < 3 for a,b in zip(report, report[1:])


# f_t = [False, True]

# print(all(f_t))