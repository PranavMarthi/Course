import random

heads_counter = 0
tails_counter = 0

for i in range(300):
    flip = random.choice(["heads", "tails"])
    if flip == "heads":
        heads_counter += 1
    else:
        tails_counter += 1

print(heads_counter)
print(tails_counter)
