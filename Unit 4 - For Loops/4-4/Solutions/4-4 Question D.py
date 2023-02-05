import random

point = random.randint(1, 6)
while True:
    count = 0
    #print(point)
    while True:
        roll = random.randint(1,6)
        count += 1
        #print(roll)
        if point == roll:
            break
    print("It took %i rolls." %count)
    answer = input("Do you wish to play again. (Y/N)")
    if answer == "N":
        break
    