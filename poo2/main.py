import cardList
import random

suits = ['hearts', 'clubs', 'diamonds', 'spades']

def getScore(players, boardCards):
    def isRoyalFlush(cards):
        ref = 0
        for suit in suits:
            royalCards = [vars(Card(suit, 'A')), vars(Card(suit, 'K')), vars(Card(suit, 'Q')), vars(Card(suit, 'J')), vars(Card(suit, '10'))]
            for royalCard in royalCards:
                print(royalCards)
                if royalCard in cards:
                    ref += 1
                    if ref == 5:
                        return True
                else:
                    ref = 0
                    break;
        return False    
    
    finalBoard = [players.get('card1'), players.get('card2'), ]
    for idx in range(0, 5):
        finalBoard.append(boardCards[idx])
    
    if isRoyalFlush(finalBoard):
        return 10

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