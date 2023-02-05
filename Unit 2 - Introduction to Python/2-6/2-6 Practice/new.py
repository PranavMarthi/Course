input_string = input("Enter the word you would like to change to Van Rooyen language: ")

last_character = input_string[-1]
print(last_character)
x = input_string.find(last_character, len(input_string))
print(x)

new_string = last_character + input_string.replace(input_string[x], "") + "mouse"

print(new_string)

