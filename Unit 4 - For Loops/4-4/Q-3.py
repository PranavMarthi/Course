import random

heads_counter = 0
tails_counter = 0
same = 0

for i in range(10000000):
    flip = random.choice(["heads", "tails"])
    if flip == "heads":
        heads_counter += 1
    else:
        tails_counter += 1

    if heads_counter == tails_counter:
        same += 1

print(same)
