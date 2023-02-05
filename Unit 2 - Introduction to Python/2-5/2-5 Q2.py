import math

x1 = input("Enter a x1 point: ")
y1 = input("Enter a y1 point: ")
x2 = input("Enter a x2 point: ")
y2 = input("Enter a y2 point: ")

distance = math.dist([int(x1), int(y1)], [int(x2), int(y2)])
# OR
diffX = int(x2) - int(x1)
diffY = int(y2) - int(y1)

distSq = diffX ** 2 + diffY ** 2
dis = math.sqrt(distSq)

print("The distance between the points (%s, %s) and (%s and %s) is %.2f" % (x1, y1, x2, y2, dis))
