def magnitude(n):
    if n >= 0:
        return "Positive"
    else:
        return "Negative"


positive_or_negative = int(input("Enter a number: "))

print(magnitude(positive_or_negative))
