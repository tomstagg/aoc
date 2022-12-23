opp_decrypt_map = {"A": "Rock", "B": "Paper", "C": "Scissors"}
my_decrypt_map = {"X": "Lose", "Y": "Draw", "Z": "Win"}


def _calc_score(opp_play, my_play):
    shape_score = {"Rock": 1, "Paper": 2, "Scissors": 3}
    return _result(opp_play, my_play) + shape_score[my_play]


def _response(opp_play, my_play):
    opp = opp_decrypt_map[opp_play]
    required_result = my_decrypt_map[my_play]

    if required_result == "Draw":
        return (opp, opp)

    if opp == "Rock":
        my = "Paper" if required_result == "Win" else "Scissors"
    if opp == "Paper":
        my = "Scissors" if required_result == "Win" else "Rock"
    if opp == "Scissors":
        my = "Rock" if required_result == "Win" else "Paper"
    return (opp, my)


def _result(opp, my):
    if opp == my:
        return 3
    if (
        (opp == "Rock" and my == "Scissors")
        or (opp == "Scissors" and my == "Paper")
        or (opp == "Paper" and my == "Rock")
    ):
        return 0
    else:
        return 6


with open("input") as f:
    strategy = f.read().splitlines()


total = []
for item in strategy:
    input = item.split(" ")
    opp, my = _response(input[0], input[1])
    total.append(_calc_score(opp, my))
    # print(opp, my)


# print(sum(total))



numbers = [1,2,3,4,5]
squared = []

for num in numbers:
    squared.append(num ** 2)

def square(number):
    return number ** 2

print (squared)

print (numbers.index)
print(list(map(square, numbers)))
