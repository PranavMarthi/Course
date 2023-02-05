length = int(input("Enter the length of the rectangle: "))
height = int(input("Enter the height of the rectangle: "))

area = length * height
perimeter = 2 * (length + height)

if area > perimeter:
    print("The area is greater than the perimeter.")
elif perimeter < area:
    print("The area is lower than the perimeter.")
else:
    print("The area is equal to the perimeter")