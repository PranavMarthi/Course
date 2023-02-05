input_string = input("Enter the word you would like to convert to Latin: ")

last_character = input_string[0]

input_string_latin = input_string.replace(input_string[0], "")

input_string = input_string_latin + last_character + "a"

print(input_string)