import random

continuething = True

while continuething:
    print("Roll your die!")
    roll = random.choice([1, 2, 3, 4, 5, 6])
    check = random.choice([1, 2, 3, 4, 5, 6])

    val = roll

    counter = 0

    while True:
        check = random.choice([1, 2, 3, 4, 5, 6])
        if roll == check:
            break
        else:
            counter += 1

    print("Got in ", counter, "tries.")

    continuepls = input("Would you like to continue? ")

    if continuepls.lower() == "no":
        continuething = False


