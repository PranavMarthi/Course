import random

all_possibilities = []
possibilities_suite = ["Heart", "Diamond", "Spade", "Clubs"]

for i in possibilities_suite:

    for j in range(1, 14):
        if j == 1 or j == 13:
            j = "A"
        elif j == 12:
            j = "King"
        elif j == 11:
            j = "Queen"
        elif j == "J":
            j = "Jack"

        string_j = str(j) + " of " + i
        all_possibilities.append(string_j)


player_1 = []

player_2 = []

for k in range(5):
    random_card1 = random.randint(0, len(all_possibilities) - 1)
    player_1.append(all_possibilities[random_card1])
    del random_card1

for k in range(5):
    random_card2 = random.randint(0, len(all_possibilities) - 1)
    player_2.append(all_possibilities[random_card2])
    del random_card2


print(player_1)
print(player_2)




