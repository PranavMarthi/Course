def findSlope(x1, x2, y1, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope


print("Slope (m): " + str(findSlope(0, 1, 0, 1)))
