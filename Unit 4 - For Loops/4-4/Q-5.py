import random

suite = random.choice(["Heart", "Clubs", "Spades", "Diamonds"])
card = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King", "A"])

print(card + " of " + suite)