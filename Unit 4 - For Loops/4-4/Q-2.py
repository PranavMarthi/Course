import random

five_counter = 0

for i in range(1000):
    roll = random.choice([1, 2, 3, 4, 5, 6])
    if roll == 5:
        five_counter += 1

print(five_counter)
