import random

headCount = 0
#tailCount = 0
totalFlips = 1000000
for i in range(totalFlips):
    flip= random.choice(["heads", "tails"])
    if flip == "heads":
        headCount += 1
    #else:
        #tailCount += 1
print("Heads:", headCount, "Tails", totalFlips - headCount)