import cardList
import random

suits = ['hearts', 'clubs', 'diamonds', 'spades']

def filter_by_suit(suit, cards):
    withMySuit = []
    for card in cards:
        hasMySuit = card.get('suit') == suit
        if not hasMySuit:
            continue
        withMySuit.append(card)
    return withMySuit

def isStraight(cards):
    sequenceMap = {'A': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, '10': None, 'J': None, 'Q': None, 'K': None}
    for card in cards:
        cardType = card['cardType']
        sequenceMap[cardType] = True
    ref = 0
    for flag in sequenceMap.values():
        if flag:
            ref += 1
            if ref == 5:
                return True
        else:
            ref = 0
    return False

def getScore(players, boardCards):
    def isRoyalFlush(cards):
        ref = 0
        for suit in suits:
            royalCards = [vars(Card(suit, 'A')), vars(Card(suit, 'K')), vars(Card(suit, 'Q')), vars(Card(suit, 'J')), vars(Card(suit, '10'))]
            for royalCard in royalCards:
                if royalCard in cards:
                    ref += 1
                    if ref == 5:
                        return True
                else:
                    ref = 0
                    break;
        return False    
    def isStraightFlush(cards):
        for suit in suits:
            filteredBySuit = filter_by_suit(suit, cards)
            if isStraight(filteredBySuit):
                return True
        return False

        
    finalBoard = [players.get('card1'), players.get('card2'), ]
    for idx in range(0, 5):
        finalBoard.append(boardCards[idx])
    
    if isRoyalFlush(finalBoard):
        return 10
    elif isStraightFlush(finalBoard):
        return 9

    return ''

class Card:
    def __init__(self, suit, cardType):
        self.suit = suit
        self.cardType = cardType

class Cards:
    def __init__(self):
        self.all = self.getCards()
        self.boardCards = self.getBoardCards()
        
    def getCards(self):
        allCards = cardList.getAll()
        cards = []
        for suit in suits:
            for card in allCards:
                cards.append(vars(Card(suit, card[0])))
        random.shuffle(cards)
        return cards

    def getCardPair(self):
        card1 = self.all.pop()
        card2 = self.all.pop()
        
        return {'card1': card1, 'card2': card2, 'score': 0}

    def getBoardCards(self):
        board = {}
        for card in range(0, 5):
            board[card] = self.all.pop()
        return board

while True:
    try:
        cards = Cards()
        playerAmt = int(input('Quantidade de jogadores: '))
        players = {}
        for idx in range(playerAmt):
            players[idx] = cards.getCardPair()

        for player in players:
            players[player]['score'] = getScore(players[player], cards.boardCards)
    except Exception:
        break