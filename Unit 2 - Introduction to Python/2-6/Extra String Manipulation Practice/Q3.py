input_string = input("Enter the word you would like to change to Van Rooyen language: ")

last_character = input_string[-1]

new_string = last_character + input_string[:len(input_string)-1] + "mouse"

print(new_string)
