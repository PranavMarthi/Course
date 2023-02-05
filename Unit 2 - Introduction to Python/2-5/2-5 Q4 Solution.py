# getting input for the products and their prices
product1 = input("Please enter the first product: ")
price1 = float(input("Please enter the cost of the " + product1 + ": $"))
product2 = input("Please enter the second product: ")
price2 = float(input("Please enter the cost of the " + product2 + ": $"))
product3 = input("Please enter the third product: ")
price3 = float(input("Please enter the cost of the " + product3 + ": $"))


# calculate total cost of these purchases
totalPrice = price1 + price2 + price3
hst = totalPrice * 0.13
total = totalPrice + hst

print("WOSS Gift Shop Receipt")
print("--------------------------")
print("%-10s\t\t%6.2f" % (product1, price1))
print("%-10s\t\t%6.2f" % (product2, price2))
print("%-10s\t\t%6.2f" % (product3, price3))
print("--------------------------")
print("HST (13%%):\t\t%6.2f" % hst)
print("--------------------------")
print("TOTAL\t\t\t%6.2f" % total)





