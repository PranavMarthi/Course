number = input("Please enter a three digit number: ")

opposite_input = int(number[-1] + number[-2] + number[-1 * len(number)])

sum_numbers = int(number) + opposite_input

print(sum_numbers)

