import math

radius = int(input("Please enter the radius: "))

circle_area = round(math.pi * (radius**2),1)
circle_circumference = round(math.pi * 2 * radius,1)

print("A circle with radius",  radius, "cm has a circumference of", circle_circumference, "cm and an area of", circle_area, "cm^2.")