myArr = []

for i in range(10):
    user_val = int(input("Please enter a number: "))
    myArr.append(user_val)

myArr.sort()


middle = int(len(myArr)/2)
print(middle)
median = 0

if len(myArr) % 2 == 1:
    median = myArr[middle]
else:
    median = (myArr[middle - 1] + myArr[middle])/2

print("Median is: " + str(median))



