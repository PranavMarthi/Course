pay_rate = 10.25 # initial pay
# ask the user for the number of hours
hours = int(input("Enter the number of hours you worked: "))

total_pay = hours * pay_rate
# money two decimal places

# Output to the screen
print("A student works for %i hours at $%.2f/hour. Their pay is $%.2f." % (hours, pay_rate, total_pay))

# print("A student works for", hours, "hours at $" + str(pay_rate) + "/hour.  Their pay is $" +
#       str(round(total_pay, 2)) + ".")
