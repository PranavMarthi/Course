import random

numFlips = 10000
numSame = 0

for i in range(numFlips):
    flip1 = random.choice(["heads", "tails"])
    flip2 = random.choice(["heads", "tails"])
    if flip1 == flip2:
        numSame += 1
print(numSame)