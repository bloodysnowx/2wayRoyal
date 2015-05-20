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
        return False

    def is2Pair(self):
        return self.sortedCountOfRank[0:3] == [2, 2, 1]

    def get2Pair(self):
        if self.is2Pair():
            return flatten([self.getXrankCards(ranks[self.countOfRank.index(2)]), self.getXrankCards(ranks[len(ranks) - 1 - list(reversed(self.countOfRank)).index(2)])])
        return False

    def is1Pair(self):
        return self.sortedCountOfRank[0:4] == [2, 1, 1, 1]

    #1 Pair 	22; 33; 44; 55; 66; 77; 88; 99; TT
    def get1Pair(self):
        if self.is1Pair():
            return self.getXrankCards(ranks[self.countOfRank.index(2)])
        return False

    #1 Pair 	JJ; QQ; KK; AA
    def isJackOrBetter(self):
        jackOrBetter = flatten([[self.countOfRank[0]], self.countOfRank[10:]])
        if sorted(jackOrBetter)[0] == 2:
            return True
        return False

    def getXtoYranksFlush(self, x, yRanks):
        for suit in suits:
            hits = flatten(map(lambda rank: filter(lambda card: card.isEqual(suit, rank), self.cards), yRanks))
            if len(hits) == x:
                return hits
        return False
        
    def get4toHighRoyal(self):
        return self.getXtoYranksFlush(4, aHighRanks)
        
    def get4toLowRoyal(self):
        return self.getXtoYranksFlush(4, ranks[1:6])

    #4 to a Straight Flush 	A234; A235; A245; A345; 3457; 3467; 3567; 4567; 4568; 4578; 4678; 5678;5679; 5689; 5789; 6789; 678T; 679T; 689T; 789T; 789J; 78TJ; 79TJ; 89TJ;89TQ; 89JQ; 8TJQ; 9TJQ; 9TJK; 9TQK; 9JQK
    def get4toStraightFlush(self):
        for xRanks in (map(lambda i: ranks[i:i+5], range(9)) + [aHighRanks]):
            ret = self.getXtoYranksFlush(4, xRanks)
            if ret != False:
                return ret
        return False

    #3 to a Royal Flush 	TJA; TJQ; TJK; TQA; TQK; TKA; JQA; JQK; JKA; QKA
    def get3toHighRoyal(self):
        return self.getXtoYranksFlush(3, aHighRanks)

    #3 to a Straight Flush 	234; 235; 236; 245; 246; 256; 345; 346; 356; 456
    def get3toLowRoyal(self):
        return self.getXtoYranksFlush(3, ranks[1:6])

    def getXtoFlush(self, x):
        if self.sortedCountOfSuit[0] == x:
            return filter(lambda card: card.suit == suits[self.countOfSuit.index(x)], self.cards)
        return False

    #4 to a Flush 	237A; 2378; 2379; 237T; 237J; 237Q; 237K; 238A; 2389; 238T; 238J; 238Q...
    def get4toFlush(self):
        return self.getXtoFlush(4)

    def getXtoYranks(self, x, yRanks):
        hits = flatten(map(lambda rank: filter(lambda card: card.rank == rank, self.cards), yRanks))
        if len(hits) == x:
            return hits
        return False

    #4 to a Straight 	TJQK
    def getTJQK(self):
        return self.getXtoYranks(4, ranks[9:13])

    #4 to a Straight 	2345; 3456; 4567; 5678; 6789; 789T; 89TJ; 9TJQ
    def getOESD(self):
        for xRanks in map(lambda i: ranks[i:i+4], range(1, 9)):
            ret = self.getXtoYranks(4, xRanks)
            if ret != False:
                return ret
        return False

    #3 to a Straight Flush 	89J; 8TJ; 8JQ; 9TJ; 9TQ; 9JQ        
    def get3toStraightFlushA(self):
        for xRanks in [[ranks[7], ranks[8], ranks[10]], [ranks[7], ranks[9], ranks[10]], [ranks[7], ranks[10], ranks[11]], [ranks[8], ranks[9], ranks[10]], [ranks[8], ranks[9], ranks[11]], [ranks[8], ranks[10], ranks[11]]]:
            ret = self.getXtoYranksFlush(3, xRanks)
            if ret!= False:
                return ret
        return False

    #4 to a Straight 	JQKA
    def getJQKA(self):
        return self.getXtoYranks(4, flatten([[ranks[0]], ranks[10:13]]))

    #3 to a Straight Flush 	9JK; 9QK
    def get3toStraightFlushB(self):
        for xRanks in [[ranks[8], ranks[10], ranks[12]], [ranks[8], ranks[11], ranks[12]]]:
            ret = self.getXtoYranksFlush(3, xRanks)
            if ret!= False:
                return ret
        return False

    #2 to a Royal Flush 	JA; JQ; JK; QK
    def get2toHighRoyalA(self):
        for xRanks in [[ranks[10], ranks[0]], ranks[10:12], [ranks[10], ranks[12]], ranks[11:]]:
            ret = self.getXtoYranksFlush(3, xRanks)
            if ret!= False:
                return ret
        return False

    #3 to a Straight Flush 	567; 678; 789; 89T
    def get3toStraightFlushC(self):
        for xRanks in map(lambda i: ranks[i:i+4], range(4, 8)):
            ret = self.getXtoYranks(3, xRanks)
            if ret != False:
                return ret
        return False

    #2 to a Royal Flush 	QA; KA
    def get2toHighRoyalA(self):
        for xRanks in [[ranks[11], ranks[0]], [ranks[12], ranks[0]]]:
            ret = self.getXtoYranksFlush(2, xRanks)
            if ret != False:
                return ret
        return False

    #4 to a Straight 	9JQK; TJQA; TJKA; TQKA
    def get4toStraightA(self):
        for xRanks in [[ranks[8]] + ranks[10:], ranks[9:12] + [ranks[0]], ranks[9:11] + [ranks[12]] + [ranks[0]], [ranks[9]] + ranks[11:] + [ranks[0]]]:
            ret = self.getXtoYranks(4, xRanks)
            if ret != False:
                return ret
        return False
    
    #3 to a Straight 	JQK
    def getJQK(self):
        return self.getXtoYranks(3, ranks[10:])

    #2 to a Straight 	JQ
    def getJQ(self):
        return self.getXtoYranks(2, ranks[10:12])

    #3 to a Straight Flush 	A23; A24; A25; A34; A35;
    # A45; 568; 578; 689; 78J;
    # 79J; 7TJ; 89Q; 8TQ; 9TK
    def get3toStraightFlushD(self):
        for xRanks in [ranks[:3], ranks[:2] + ranks[3:4], ranks[:2] + ranks[4:5], ranks[0:1] + ranks[2:4], [ranks[0], ranks[2], ranks[4]],
                       ranks[0:1] + ranks[3:5], ranks[4:6] + ranks[7:8], ranks[4:5] + ranks[6:8], ranks[5:6] + ranks[7:9], ranks[6:8] + ranks[10:11],
                       [ranks[6], ranks[8], ranks[10]], ranks[6:7] + ranks[9:11], ranks[7:9] + ranks[11:12], [ranks[7], ranks[9], ranks[11]], ranks[8:10], ranks[12:]]:
            ret = self.getXtoYranksFlush(3, xRanks)
            if ret != False:
                return ret
        return False

    #2 to a Straight 	JK
    def getJK(self):
        return self.getXtoYranks(2, [ranks[10], ranks[12]])
    
    #2 to a Royal Flush 	TJ
    def getTJsuited(self):
        return self.getXtoYranksFlush(2, ranks[9:11])
    
    #3 to a Straight Flush 	457; 467; 679; 78T; 79T
    def get3toStraightFlushE(self):
        for xRanks in [ranks[3:5] + ranks[6:7], ranks[3:4] + ranks[5:7], ranks[5:7] + ranks[8:9], ranks[6:8] + ranks[9:10], ranks[6:7] + ranks[8:10]]:
            ret = self.getXtoYranksFlush(3, xRanks)
            if ret != False:
                return ret
        return False
    
    #2 to a Straight 	JA; QK
    def getJAorQK(self):
        for xRanks in [[ranks[10], ranks[0]], ranks[11:13]]:
            ret = self.getXtoYranks(2, xRanks)
            if ret != False:
                return ret
        return False
    
    #2 to a Straight 	QA; KA
    def getQAorKA(self):
        for xRanks in [[ranks[11], ranks[0]], [ranks[12], ranks[0]]]:
            ret = self.getXtoYranks(2, xRanks)
            if ret != False:
                return ret
        return False

    #2 to a Royal Flush 	TQ
    def getTQsuited(self):
        return self.getXtoYranksFlush(2, [ranks[9], ranks[11]])
    #Single Card 	a Jack; a Queen; a King; an Ace
    def getSingleJackOrBetter(self):
        for xRanks in [[ranks[0]], [ranks[12]], [ranks[11]], [ranks[10]]]:
            ret = self.getXtoYranks(1, xRanks)
            if ret != False:
                return ret
        return False
    #3 to a Straight Flush 	347; 357; 367; 458; 468; 478; 569; 579; 589; 67T; 68T; 69T
    def get3toStraightFlushF(self):
        for xRanks in [ranks[2:4] + ranks[6:7], [ranks[2], ranks[4], ranks[6]], ranks[2:3] + ranks[5:7], ranks[3:5] + ranks[7:8], [ranks[3], ranks[5], ranks[7]], ranks[3:4] + ranks[6:8], ranks[4:6] + ranks[8:9], [ranks[4], ranks[6], ranks[8]], ranks[4:5] + ranks[7:9], ranks[5:7] + ranks[9:10], [ranks[5], ranks[7], ranks[9]], ranks[5:6] + ranks[8:10]]:
            ret = self.getXtoYranksFlush(3, xRanks)
            if ret != False:
                return ret
        return False
    #2 to a Straight Flush 	45; 56
    def get45or56suited(self):
        for xRanks in [ranks[3:5], ranks[4:6]]:
            ret = self.getXtoYranksFlush(2, xRanks)
            if ret != False:
                return ret
        return False

    def getTKsuited(self):
        return self.getXtoYranksFlush(2, [ranks[9], ranks[12]])
    
    def getKA(self):
        return self.getXtoYranks(2, [ranks[12], ranks[0]])

    def getQA(self):
        return self.getXtoYranks(2, [ranks[11], ranks[0]])

    def getJA(self):
        return self.getXtoYranks(2, [ranks[10], ranks[0]])

    def get7TJsuited(self):
        return self.getXtoYranks(3, ranks[6:7] + ranks[9:11])
    
    def get78Jsuited(self):
        return self.getXtoYranks(3, ranks[6:8] + ranks[10:11])

    def get79Jsuited(self):
        return self.getXtoYranks(3, [ranks[6], ranks[8], ranks[10]])
    
    
class Card:
    def __init__(self, suit, rank, pos):
        self.suit = suit
        self.rank = rank
        self.pos = pos

    def __str__(self):
        return "suit: " + self.suit + ", rank:" + self.rank + ", pos:" + str(self.pos)

    def isEqual(self, suit, rank):
        return self.suit == suit and self.rank == rank
