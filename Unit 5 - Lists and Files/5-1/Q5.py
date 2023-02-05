# import random
#
# friends_list = ["tim", "donald", "jack", "tom", "bob"]
# emotions = ["loves", "hates", "misses", "likes", "envies"]
#
# for i in friends_list:
#     random_emotion = random.choice(emotions)
#     random_friends = random.choice(friends_list)
#
#     expression = str(i) + " " + str(random_emotion) + " " + str(random_friends)
#
#     print(expression)
#


import random

friends_list = ["tim", "donald", "jack", "tom", "bob"]
emotions = ["loves", "hates", "misses", "likes", "envies"]

for i in friends_list:
    random_emotion = random.choice(emotions)
    temp = ["tim", "donald", "jack", "tom", "bob"]
    temp.remove(i)
    random_friends = random.choice(temp)

    temp = friends_list
    
    expression = str(i) + " " + str(random_emotion) + " " + str(random_friends)

    print(expression)

