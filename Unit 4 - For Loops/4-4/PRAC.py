string = input("Please enter a sentence: ")

for i in range(len(string)):
    print(string[i], string[len(string) - 1 - i])