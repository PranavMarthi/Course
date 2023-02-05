import random

list1 = []

random_length = random.randint(1, 10)

for i in range(random_length):
    random_index = random.randint(1, 15)
    list1.append(random_index)

list2 = []

random_length2 = random.randint(1, 10)

for i in range(random_length2):
    random_index2 = random.randint(1, 15)
    list2.append(random_index2)

list1.sort()
list2.sort()

print(list1)
print(list2)

final_list = []

length_list1 = len(list1)
length_list2 = len(list2)

smaller_list = []

if length_list1 < length_list2:
    smaller_list = list1
else:
    smaller_list = list2


for i in range(len(smaller_list)):
    print(list1[i], "COMPARE")

    if list1[i] > list2[i]:
        print(list2[i], "LOWER")
        final_list.append(list2[i])
    elif list1[i] < list2[i]:
        print(list1[i])
        final_list.append(list1[i])
    else:
        print("EQUAL", list2[i])

print(final_list)

# import random
#
# list1 = []
#
# for i in range(random.randint(8, 12)):
#     list1.append(random.randint(1, 100))
#
# list2 = []
#
# for i in range(random.randint(4, 7)):
#     list2.append(random.randint(1, 100))
#
# list1.sort()
# list2.sort()
#
# print(list1)
# print(list2)
#
# list3 = []
#
# while True:
#     if len(list1) == 0 or len(list2) == 0:
#         break
#     if list1[0] < list2[0]:
#         list3.append((list1[0]))
#         del list1[0]
#     else:
#         list3.append(list2[0])
#         del list2[0]
#
# if len(list1) > 0:
#
#     for val in list1:
#         list3.append(val)
#
#
# print(list1)
# print(list2)
# print(list3)
#
