# user_sentence = input("Please enter a sentence: ")
#
# odd_sentence = ""
# even_sentence = ""
#
# new_sentence = ""
#
# for i in user_sentence:
#
#     if i == " ":
#         new_sentence += 'mouse'
#     else:
#         new_sentence += i
#
# for i in range(len(new_sentence)):
#
#     if i % 2 == 0:
#         even_sentence += new_sentence[i]
#     else:
#         odd_sentence += new_sentence[i]
#
# print("even_sentence", even_sentence)
# print("odd_sentence", odd_sentence)

# arr = []
#
# for i in range(100):
#     arr.append(False)
#
#
# for k in range(1, 101):
#
#     for j in range(k, 101, k):
#
#         if not arr[j-1]:
#             arr[j-1] = True
#         else:
#             arr[j-1] = False
#
# countOpen = 0
# countClose = 0
#
# for i in range(len(arr)):
#     if arr[i]:
#         countOpen += 1
#         print(i + 1, "is open")
#     else:
#         countClose += 1
#         print(i + 1, "is closed")
#
# print(arr)
# print("There are %i open doors" % countOpen)
# print("There are %i closed doors" % countClose)

arr = []

num_of_lockers = 10000

for i in range(num_of_lockers):
    arr.append(False)


for k in range(1, num_of_lockers+1):

    for j in range(k, num_of_lockers+1, k):

        if not arr[j-1]:
            arr[j-1] = True
        else:
            arr[j-1] = False

countOpen = 0
countClose = 0

for i in range(len(arr)):
    if arr[i]:
        countOpen += 1
        print(i + 1, "is open")
    # else:
    #     countClose += 1
    #     print(i + 1, "is closed")

print("There are %i open doors" % countOpen)
print("There are %i closed doors" % countClose)
