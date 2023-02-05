locker_combination = input("Enter your locker combination: ")
index = 0

while index < len(locker_combination):

    index = locker_combination.find("-", index)
    if index == -1:
        break
    print(locker_combination + ' found at', index)

    index += 1
