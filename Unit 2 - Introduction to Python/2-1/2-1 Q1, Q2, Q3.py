# My First Python Program
# By Mr. Van Rooyen
# September 11, 2022

counter = 0  # initialize the variable counter as 0

# the following line of code does the following:
# creates a variable called firstName
# prompts the user
# gets input from the keyboard - all in just one line...amazing
firstName = input("Please enter your first name:")
# gets the user's first name
age = input("Please enter your age:")

# start of a while loop
while counter < 10:  # repeat as long as counter is less than 10
    print("NAME:" + firstName, "AGE:" + age)  # display the firstName
    counter = counter + 1  # add one to the variable counter
