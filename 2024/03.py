"""Day 03: Mull It Over"""
from re import findall


data = open("./resources/03.txt").read()

candidate = ""
result_1, result_2 = [],[]
capture = False
do = True

for i in range(len(data)):
    if capture and (data[i].isdigit() or data[i] in [",",")"]):
        candidate += str(data[i])
        if data[i] == ")" and "," in candidate:
            result_1.append(candidate[:-1].split(","))
            if do:
                result_2.append(candidate[:-1].split(","))
            capture = False
            candidate = ""
    else:
        capture = False
        candidate = ""

    if data[i-3:i+1] == "mul(":
        capture = True
    if data[i-3:i+1] == "do()":
        do = True
    if data[i-6:i+1] == "don't()":
        do = False

print("result_1", sum(int(x) * int(y) for x,y in result_1))
print("result_2", sum(int(x) * int(y) for x,y in result_2))


# another way #1
# from parse import findall
# d = "do()" + open("./resources/03.txt").read() + "don't()"
# for _ in 1, 2:
#     print(sum(x*y for x,y in findall("mul({:d},{:d})", d)))
#     d = ''.join(r[0] for r in findall("do(){}don't()", d))

# another way #2


result_1 = sum(int(a) * int(b) for a, b in findall(r"mul\((\d+),(\d+)\)", data))

enabled = True

result_2 = 0
for a, b, do, dont in findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data):
    if do or dont: 
        enabled = bool(do)
    else:
        result_2 += int(a)* int(b) * enabled
 

print("result_1", result_1)
print("result_2", result_2)