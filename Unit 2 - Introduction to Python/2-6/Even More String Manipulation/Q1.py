# 9 digit conversion

number = input("Please enter a 9-digit number: ")

comma_seperated_version = number[:3] + "," + number[3:6] + "," + number[6:]

print(comma_seperated_version)



