import random

randInt = random.randrange(1, 101)
print(randInt)
# user_input = int(input("Enter a number: "))
contPLS = True
counter = 1

while contPLS:

    user_input = int(input("Enter a number: "))

    if user_input > randInt:
        print("Too big")
        counter += 1
    elif user_input < randInt:
        print("Too small")
        counter += 1
    else:
        contPLS = False


print("You guessed in", counter, "tries")

