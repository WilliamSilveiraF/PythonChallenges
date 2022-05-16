import cardList
import random

class Card:
    def __init__(self, suit, cardType):
        self.suit = suit
        self.cardType = cardType

class Cards:
    def __init__(self, amtPlayers):
        self.all = self.getCards()
        self.players = self.getPlayers(amtPlayers)

    def getCards(self):
        suits = ['hearts', 'clubs', 'diamonds', 'spades']
        allCards = cardList.getAll()
        cards = []

        for suit in suits:
            for card in allCards:
                cards.append(vars(Card(suit, card[0])))
        return cards

    def sortCards(self):
        random.shuffle(self.all)

    def getPlayers(self, amtPlayers):
        self.sortCards()
        cardsAmt = len(self.all) // amtPlayers
        players = {}
        for player in range(0, amtPlayers):
            players[player] = []
            for _ in range(0, cardsAmt):
                card = self.all.pop()
                players[player].append(card)
        return players

cards = Cards(amtPlayers=9)

print(cards.players)