
def part_1(data):
    total = 0
    for assignment in data:
        total += 1 if check_contained(assignment) else 0
    print(total)

    # alternatively using map with sum working on booleans:
    # print(sum(list(map(check_contained, data))))

def part_2(data):
    print(sum(list(map(check_overlap,data))))

def check_contained(assignment) -> bool:
    first_start, first_end = map(int, assignment.split(',')[0].split('-'))
    second_start, second_end = map(int, assignment.split(',')[1].split('-'))

    return (second_start >= first_start and second_end <= first_end) or \
        (first_start >= second_start and first_end <= second_end) 


def check_overlap(assignment) -> bool:
    first_start, first_end = map(int, assignment.split(',')[0].split('-'))
    second_start, second_end = map(int, assignment.split(',')[1].split('-'))
    print(assignment)
    return first_end >= second_start and first_start <= second_end

data = open("input.txt").read().splitlines()
part_1(data)
part_2(data)



