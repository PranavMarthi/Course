def findSlope(x1, y1, x2, y2):
    diffy = y2 - y1
    diffx = x2 - x1
    slope = diffy/diffx
    return slope

m = findSlope(-3, 5, 7, 12)
print(m)