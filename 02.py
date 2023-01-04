opp_decrypt_map = {"A": "Rock", "B": "Paper", "C": "Scissors"}
my_decrypt_map = {"X": "Rock", "Y": "Paper", "Z": "Scissors"}


def calc_score(opp_play, my_play):
    shape_score = {"Rock": 1, "Paper": 2, "Scissors": 3}
    return _result(opp_play, my_play) + shape_score[my_decrypt_map[my_play]]


def _result(opp_play, my_play):
    opp = opp_decrypt_map[opp_play]
    my = my_decrypt_map[my_play]

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
    total.append(calc_score(input[0], input[1]))


print(sum(total))
