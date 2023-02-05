import random

numRolls = 1000000
countFive = 0

for i in range(numRolls):
    roll = random.randint(1, 6)
    if roll == 5:
        countFive += 1
print(countFive/numRolls)

