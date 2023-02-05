import random

contestant_vals = [0, 0, 0, 0, 0, 0]

for i in range(1000):
    randINT = random.randint(0, 5)

    contestant_vals[randINT] += 1

print(contestant_vals)