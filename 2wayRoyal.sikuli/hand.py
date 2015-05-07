suits = ["s", "h", "d", "c"]
ranks = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]
#from itertools import chain
#aHighRanks = list(chain.from_iterable([[ranks[0]], ranks[9:13]]))
aHighRanks = [item for sublist in [[ranks[0]], ranks[9:13]] for item in sublist]

class Hand:
    def __init__(self, cards):
        self.cards = []
        map(lambda card: self.cards.append(Card(card[0], card[1], card[2])), cards)

    def __str__(self):
        return reduce(lambda x, y: str(x) + ", " + str(y), self.cards)
        
    def isFlush(self):
        aSuit = self.cards[0].suit
        return len(filter(lambda card:card.suit == aSuit, self.cards)) == 5

    def isAHighStraight(self):
        for rank in aHighRanks:
            if len(filter(lambda card:card.rank == rank, self.cards)) != 1:
                return False
        return True

    def isHighRoyal(self):
        return self.isFlush() and self.isAHighStraight()

class Card:
    def __init__(self, suit, rank, pos):
        self.suit = suit
        self.rank = rank
        self.pos = pos

    def __str__(self):
        return "suit: " + self.suit + ", rank:" + self.rank + ", pos:" + str(self.pos)
