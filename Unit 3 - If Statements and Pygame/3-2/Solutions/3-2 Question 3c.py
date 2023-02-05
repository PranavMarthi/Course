def breakApart(ptStr):
    comma = ptStr.find(",")
    print(comma)
    xVal = int(ptStr[1:comma])
    yVal = int(ptStr[comma + 1:-1])
    print(yVal)
    return xVal, yVal
    
    
x, y = breakApart("(-31,       5)")
print(2*x, 3*y)