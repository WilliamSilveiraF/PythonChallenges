import cardList
import random

suits = ['hearts', 'clubs', 'diamonds', 'spades']

def count_by_cardType(cards):
    sequenceMap = {'A': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, 'J': 0, 'Q': 0, 'K': 0}
    for card in cards:
        cardType = card['cardType']
        sequenceMap[cardType] += 1

    return sequenceMap

def filter_by_suit(suit, cards):
    withMySuit = []
    for card in cards:
        hasMySuit = card.get('suit') == suit
        if not hasMySuit:
            continue
        withMySuit.append(card)
    return withMySuit

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

    def isStraightFlush(cards):
        for suit in suits:
            filteredBySuit = filter_by_suit(suit, cards)
            if isStraight(filteredBySuit):
                return True
        return False

    def isFourOfAKind(cards):
        sequenceMap = count_by_cardType(cards)
        for value in sequenceMap.values():
            if value == 4:
                return True
        return False

    def isFullHouse(cards):
        hasTwoPair = False
        hasThreeOfAKind = False

        sequenceMap = count_by_cardType(cards)
        for value in sequenceMap.values():
            if value >= 3 and not hasThreeOfAKind:
                hasThreeOfAKind = True
            elif value >= 2 and not hasTwoPair:
                hasTwoPair = True
        return True if hasTwoPair and hasThreeOfAKind else False

    def isFlush(cards):
        for suit in suits:
            filteredBySuit = filter_by_suit(suit, cards)
            if len(filteredBySuit) >= 5:
                return True
        return False
    
    def areThreeOfAKind(cards):
        sequenceMap = count_by_cardType(cards)
        hasThreeOfAKind = False
        
        for value in sequenceMap.values():
            if value == 3:
                hasThreeOfAKind = True
                break
        return hasThreeOfAKind

    def areTwoPair(cards):
        sequenceMap = count_by_cardType(cards)
        pairs = 0

        for value in sequenceMap.values():
            if value == 2:
                pairs += 1
        return True if pairs >= 2 else False

    def isOnePair(cards):
        sequenceMap = count_by_cardType(cards)
        for value in sequenceMap.values():
            if value == 2:
                return True
        return False

    finalBoard = [players.get('card1'), players.get('card2')]
    for idx in range(0, 5):
        finalBoard.append(boardCards[idx])

    print(finalBoard)
    if isRoyalFlush(finalBoard):
        print("isRoyalFlush")
        return 10
    elif isStraightFlush(finalBoard):
        print("isStraightFlush")
        return 9
    elif isFourOfAKind(finalBoard):
        print("isFourOfAKind")
        return 8
    elif isFullHouse(finalBoard):
        print("isFullHouse")
        return 7
    elif isFlush(finalBoard):
        print("isFlush")
        return 6
    elif isStraight(finalBoard):
        print("isStraight")
        return 5
    elif areThreeOfAKind(finalBoard):
        print("areThreeOfAKind")
        return 4
    elif areTwoPair(finalBoard):
        print("areTwoPair")
        return 3
    elif isOnePair(finalBoard):
        print("isOnePair")
        return 2
    else:
        print("isHighCard")
        return 1

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

        scores = []
        for player in players:
            players[player]['score'] = getScore(players[player], cards.boardCards)
            scores.append(players[player]['score'])
        greater = max(scores)

        if scores.count(greater) > 1:
            tied = [i for i, x in enumerate(scores) if x == greater]
            sequenceMap = {'A': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [], 'J': [], 'Q': [], 'K': []}
            for player in tied:
                cards = players[player]
                card1 = cards.get('card1')['cardType']
                card2 = cards.get('card2')['cardType']

                if not player in sequenceMap[card1]:
                    sequenceMap[card1].append(player)
                if not player in sequenceMap[card2]:
                    sequenceMap[card2].append(player)

            sequenceMap = list(sequenceMap.values())
            sequenceMap.reverse()
            winnerIDs = []
            print(sequenceMap)
            for playersWhoHaveTheCard in sequenceMap:
                print(playersWhoHaveTheCard)
                if len(playersWhoHaveTheCard) == 0:
                    continue
                elif len(playersWhoHaveTheCard) >= 1:
                    winnerIDs = playersWhoHaveTheCard
                    break
                if len(winnerIDs) > 0:
                    break

            if len(winnerIDs) > 1:
                print(f"There is a draw between {str(winnerIDs)}")
            else:
                print(f"The winner is the player {winnerIDs[0] + 1}")
        else:
            print(f"The winner is the player {scores.index(greater) + 1}.")
        print(scores)
    except Exception:
        break