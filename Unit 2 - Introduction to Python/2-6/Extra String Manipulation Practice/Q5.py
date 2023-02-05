input_string = input("Input a word: ")
search_string = input("Search a string within this word: ")

print("The first occurrence of the search string was at position:", input_string.find(search_string))

index = 0
while index < len(input_string):

    index = input_string.find(search_string, index)
    if index == -1:
        break
    print(search_string + ' found at', index)

    index += 2  # +2 because len('ll') == 2
