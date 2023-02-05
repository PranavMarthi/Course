mark1 = input("Enter your first mark: ")
mark2 = input("Enter your second mark: ")
mark3 = input("Enter your third mark: ")
mark4 = input("Enter your fourth mark: ")
mark5 = input("Enter your fifth mark: ")

total_marks = 60

percentage_mark1 = int(mark1)/total_marks * 100
percentage_mark2 = int(mark2)/total_marks * 100
percentage_mark3 = int(mark3)/total_marks * 100
percentage_mark4 = int(mark4)/total_marks * 100
percentage_mark5 = int(mark5)/total_marks * 100

print("Mark\t\tPercent")
print("%2s %14.2f" % (mark1, percentage_mark1))
print("%2s %14.2f" % (mark2, percentage_mark2))
print("%2s %14.2f" % (mark3, percentage_mark3))
print("%2s %14.2f" % (mark4, percentage_mark4))
print("%2s %14.2f" % (mark5, percentage_mark5))


