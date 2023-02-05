import random

for i in range(5):
    suit = random.choice(["Spades", "Clubs", "Diamonds", "Hearts"])
    #card = random.choice(["Ace", "Two", "Three", ..., "King"])
    card = random.randint(1, 13)
    if card == 1:
        cardName = "Ace"
    elif card == 11:
        cardName = "Jack"
    elif card == 12:
        cardName = "Queen"
    elif card == 13:
        cardName = "King"
    else:
        cardName = str(card)
        
    string = "%s of %s" %(cardName, suit)

    print(string)