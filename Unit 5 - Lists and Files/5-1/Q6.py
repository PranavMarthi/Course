
fruits_list = ["apple", "orange", "banana", "grapes", "thing", "watermelon", "thingy", "damnit", "noidea", "sonofabitch"]

fruit_prices = [4, 5, 6, 7, 1, 2, 4, 5, 3, 7]

for i in range(len(fruit_prices)):
    print(fruits_list[i], "costs $" + str(fruit_prices[i]))
