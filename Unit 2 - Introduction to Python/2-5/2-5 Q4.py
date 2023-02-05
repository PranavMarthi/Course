item1 = input("Enter the name of item 1: ")
cost_item1 = float(input("Enter the cost of item 1: "))
item2 = input("Enter the name of item 2: ")
cost_item2 = float(input("Enter the cost of item 2: "))
item3 = input("Enter the name of item 3: ")
cost_item3 = float(input("Enter the cost of item 3: "))

tax = (cost_item1 + cost_item2 + cost_item2) * 0.13

print("WOSS Gift Shop Receipt")
print("----------------------")
print("%-10s $%1.2f" % (item1, cost_item1))
print("%-10s $%1.2f" % (item2, cost_item2))
print("%-10s $%1.2f" % (item3, cost_item3))
print("----------------------")
print("HST 13%% $%10.2f" % tax)
print("----------------------")
print("TOTAL$%10.2f" % (tax + cost_item1 + cost_item2 + cost_item3))
