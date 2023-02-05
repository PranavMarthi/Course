user_input = input("Please enter a string with at least two words: ")

# a)

print(len(user_input))

# b)

print("First character:", user_input[0])
print("Last character: ", user_input[-1])

# c)

print(user_input.count(" "))

# d)

print(user_input.upper())

# e)

print(user_input.replace("of", "mouse"))

# f)

space_index = user_input.find(" ")
print(user_input[:space_index])


