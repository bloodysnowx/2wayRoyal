suits = ["s", "h", "d", "c"]
ranks = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]
#from itertools import chain
#aHighRanks = list(chain.from_iterable([[ranks[0]], ranks[9:13]]))

def flatten(list):
    return [item for sublist in list for item in sublist]

aHighRanks = flatten([[ranks[0]], ranks[9:]])

class Hand:
    def __init__(self, cards):
        self.cards = []
        map(lambda card: self.cards.append(Card(card[0], card[1], card[2])), cards)
        self.countOfRank = self.getCountOfRank()
        self.sortedCountOfRank = sorted(self.countOfRank, reverse=True)
        self.countOfSuit = self.getCountOfSuit()
        self.sortedCountOfSuit = sorted(self.countOfSuit, reverse=True)

    def __str__(self):
        return reduce(lambda x, y: str(x) + ", " + str(y), self.cards)

    def getCountOfSuit(self):
        return map(lambda suit: len(filter(lambda card: card.suit == suit, self.cards)), suits)
        
    def isFlush(self):
        return self.sortedCountOfSuit[0] == 5

    def isAHighStraight(self):
        return self.countOfRank == [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]

    def isHighRoyal(self):
        return self.isFlush() and self.isAHighStraight()

    def isLowStraight(self):
        return self.countOfRank == [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]

    def isLowRoyal(self):
        return self.isFlush() and self.isLowStraight()

    def isStraight(self):
        if self.countOfRank.count(1) != 5:
            return False
        startIndex = self.countOfRank.index(1)
        return self.isAHighStraight() or self.countOfRank[startIndex:startIndex + 5] == [1, 1, 1, 1, 1]

    def isStraightFlush(self):
        return self.isFlush() and self.isStraight()

    def getCountOfRank(self):
        return map(lambda rank: len(filter(lambda card: card.rank == rank, self.cards)), ranks)
    
    def is4OfAKind(self):
        return self.sortedCountOfRank[0] == 4

    def isFullHouse(self):
        return self.sortedCountOfRank[0:2] == [3, 2]

    def is3OfAKind(self):
        return self.sortedCountOfRank[0:3] == [3, 1, 1]

    def getXrankCards(self, rank):
        return filter(lambda card: card.rank == rank, self.cards)
    
    def get3OfAKind(self):
        if self.is3OfAKind():
            return self.getXrankCards(ranks[self.countOfRank.index(3)])
        else:
            return False

    def is2Pair(self):
        return self.sortedCountOfRank[0:3] == [2, 2, 1]

    def get2Pair(self):
        if self.is2Pair():
            return flatten([self.getXrankCards(ranks[self.countOfRank.index(2)]), self.getXrankCards(ranks[len(ranks) - 1 - list(reversed(self.countOfRank)).index(2)])])
        else:
            return False

    def is1Pair(self):
        return self.sortedCountOfRank[0:4] == [2, 1, 1, 1]

    def get1Pair(self):
        if self.is1Pair():
            return self.getXrankCards(ranks[self.countOfRank.index(2)])
        else:
            return False

    def get4toXranksFlush(self, xRanks):
        for suit in suits:
            hits = flatten(map(lambda rank: filter(lambda card: card.isEqual(suit, rank), self.cards), xRanks))
            if len(hits) == 4:
                return hits
        return False
        
    def get4toHighRoyal(self):
        return self.get4toXranksFlush(aHighRanks)
        
    def get4toLowRoyal(self):
        return self.get4toXranksFlush(ranks[1:6])

    def get4toStraightFlush(self):
        for xRanks in (map(lambda i: ranks[i:i+5], range(9)) + [aHighRanks]):
            ret = self.get4toXranksFlush(xRanks)
            if ret != False:
                return ret
        return False

class Card:
    def __init__(self, suit, rank, pos):
        self.suit = suit
        self.rank = rank
        self.pos = pos

    def __str__(self):
        return "suit: " + self.suit + ", rank:" + self.rank + ", pos:" + str(self.pos)

    def isEqual(self, suit, rank):
        return self.suit == suit and self.rank == rank
