class Card():

    def __init__(self, suit, value)
        self.suit = suit
        self.value = value

    suit = ["Spades", "Hearts", "Clubs", "Diamonds"]
    value = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    cards = ['2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Spades', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Hearts', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs', 'Ace of Clubs', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Diamonds']
    dealtCards = []

class Deck(object):

    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Spades", "Hearts", "Clubs", "Diamonds"]:
            for value in [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]:
                self.cards.append(Card(suit, value))

    def show(self):
        for card in self.cards:
        cards.show()


    #discard card off top of deck
    def discardCard():
        dealtCard = cards.pop(0)
        return dealtCards.append(dealtCard)


    #shuffle cards
    import random
    def shuffleCards():
        random.shuffle(cards)
        return cards

    # cut deck at a specific location in the deck
    def cutDeck(cutLocation):
        return (cards[cutLocation:] + cards[:cutLocation])

    # order the remaining cards left in the deck
    def orderCards(cards, discardedCards):
        newDeck = self.Deck()
        for card in newDeck:
            if card in discardedCards:
                newDeck.remove(card)


    # build the deck again from scratch
    def rebuildDeck():
        self.Deck()
    

    

