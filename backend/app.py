suit = ["Spades", "Clubs", "Diamonds", "Hearts"]
value = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]


cards = []
#deal default cards
def defaultCards(suit, value):
    for s in suit:
        for v in value:
            cards.append(f"{v} of {s}")
defaultCards(suit, value)
print(cards)


#deal card off top of deck
def dealOneCard():
  return print(cards[0])

#shuffle cards
import random
random.shuffle(cards)
print(cards)

#function to shuffle cards but returns "None"
def shuffleCards(currentCards):
  return print(random.shuffle(currentCards))

shuffleCards(cards)

