

def group_elf_calories(calorie_items: list[str]):
    elf_calories = []
    calories = 0
    for item in calorie_items:
        if item != "":
            calories += int(item)
        else:
            elf_calories.append(calories)
            calories = 0
    return elf_calories


def main():
    with open("input") as f:
        calorie_items = f.read().splitlines()

    elf_no = 1
    top_elf = (0, 0)
    elf_calorie_total = 0

    for item in calorie_items:
        if item != "":
            elf_calorie_total += int(item)
        else:
            if elf_calorie_total > top_elf[1]:
                top_elf = (elf_no, elf_calorie_total)
            elf_calorie_total = 0
            elf_no += 1
    # print(top_elf)

    elf_calories = group_elf_calories(calorie_items)

    print(sum(sorted(elf_calories, reverse=True)[0:3]))


main()
