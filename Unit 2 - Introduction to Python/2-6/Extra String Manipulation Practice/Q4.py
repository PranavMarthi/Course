word = input("Enter Van Rooyen Language: ")

word = word.replace("mouse", "")

first_char = word[0]

word = word.replace(first_char, "")

word = word + first_char

print(word)
