import cardList
import random

class Card:
    def __init__(self, suit, cardType):
        self.suit = suit
        self.cardType = cardType

class Cards:
    def __init__(self):
        suits = ['hearts', 'clubs', 'diamonds', 'spades']
        allCards = cardList.getAll()
        self.all = []
        for suit in suits:
            for card in allCards:
                self.all.append(vars(Card(suit, card[0])))

    def sortCards(self):
        print()

cards = Cards()

cards.sortCards()

print(len(cards.all))