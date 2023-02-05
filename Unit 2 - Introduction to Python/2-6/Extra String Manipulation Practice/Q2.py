input_string = input("Enter the Latin word you would like to convert to English: ")

eliminate_a = input_string.replace(input_string[-1], "")

last_character = eliminate_a[-1]

eliminate_last_character = eliminate_a.replace(last_character, "")

final_answer = last_character + eliminate_last_character

print(final_answer)
