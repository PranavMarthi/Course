def sepCoordinates(coordinates):
    index = coordinates.find(",")

    x_coordinate = coordinates[index - 1]
    y_coordinate = coordinates[index + 2]

    return x_coordinate, y_coordinate


# ALTERNATE SOLUTION

def breakApart(ptStr):
    spot = ptStr.find(",")
    xVal = ptStr[1:spot]
    yVal = ptStr[spot + 1:-1]

    return int(xVal), int(yVal)


x1, y1 = breakApart("(3,5)")
print(x1, y1)

x, y = sepCoordinates("(2, 5)")
print(x, y)
