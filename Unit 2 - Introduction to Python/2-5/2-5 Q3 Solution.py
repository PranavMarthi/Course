# get all the marks from the user
mark1 = int(input("Please enter the first mark: "))
mark2 = int(input("Please enter the first mark: "))
mark3 = int(input("Please enter the first mark: "))
mark4 = int(input("Please enter the first mark: "))
mark5 = int(input("Please enter the first mark: "))

# calculate the individual marks
percent1 = mark1 / 60 * 100
percent2 = mark2 / 60 * 100
percent3 = mark3 / 60 * 100
percent4 = mark4 / 60 * 100
percent5 = mark5 / 60 * 100

# average marks calculation

aveMark = (mark1 + mark2 + mark3 + mark4 + mark5) / 5
avePercent = aveMark / 60 * 100

print("Mark\t\tPercent")
print("%2i\t\t\t%5.1f" % (mark1, percent1))
print("%2i\t\t\t%5.1f" % (mark2, percent2))
print("%2i\t\t\t%5.1f" % (mark3, percent3))
print("%2i\t\t\t%5.1f" % (mark4, percent4))
print("%2i\t\t\t%5.1f" % (mark5, percent5))

print("\nThe average for the test is: %.1f%%" % avePercent)
