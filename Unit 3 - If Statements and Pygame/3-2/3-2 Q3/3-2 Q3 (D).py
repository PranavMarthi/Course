import math

first_coordinate = input("Enter the first coordinate: ")
second_coordinate = input("Enter the second coordinate: ")


def sepCoordinates(coordinates):
    index = coordinates.find(",")

    x_coordinate = coordinates[index - 1]
    y_coordinate = coordinates[index + 2]

    return int(x_coordinate), int(y_coordinate)


def calculateDistance(x1, x2, y1, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def findSlope(x1, x2, y1, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope


x1, y1 = sepCoordinates(first_coordinate)
x2, y2 = sepCoordinates(second_coordinate)

print("The distance between points", first_coordinate, "and", second_coordinate, "is",
      str(round(calculateDistance(x1, x2, y1, y2))), 2)

print("The slope between points", first_coordinate, "and", second_coordinate, "is",
      str(findSlope(x1, x2, y1, y2)))
