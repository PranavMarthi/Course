# REVIEW!

name = "Bob"
bill = 45.1
print("Hi %s, your bill comes to $%.2f" % (name, bill))

# Field spacing – The field spacing is the total number of spaces used to display your value, including the ones used
# by your value. e.g.

# a = 12.3456
# n = 300
# 	s = “Joe”
# 	%10f		---12.3456	- note the decimal takes up one space
# 	%10s		-----Joe
# 	%10i		-------300
# 	%10.2f	-----12.35	- note that it will round off
# 	%-10.2f	12.35-----	- "-" will left align
# 	%2i		300			- making the field smaller than the
# 						  number of characters will not chop off
# 						  characters

# a = 12.3456
# n = "JOHN"

# print(a)
# print(n)

# print("%-10s" % n)
# print("%10s" % n)

a = 12.3456
n = 300
s = "Joe"

print("1234567890")
print("%10f" % a)
print("%10s" % s)
print("%10i" % n)

print("%-10f" % a)
print("%-10s" % s)
print("%-10i" % n)

print("%10.2f" % a)
print("%10f%10s%10i" % (a, s, n))
print("%10f\t%10s\t%10i" % (a, s, n))

print("%s lives at %s street address and makes %.2f pay per hour" % (s, n, a))
