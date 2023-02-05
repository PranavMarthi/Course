import random

dice1 = random.choice([1, 2, 3, 4, 5, 6])
dice2 = random.choice([1, 2, 3, 4, 5, 6])

poss = []

for i in range(11):
    poss.append(0)

for j in range(10000):
    dice1 = random.choice([1, 2, 3, 4, 5, 6])
    dice2 = random.choice([1, 2, 3, 4, 5, 6])
    sum = dice1 + dice2

    print(sum)

    poss[sum-2] += 1

print(poss)
