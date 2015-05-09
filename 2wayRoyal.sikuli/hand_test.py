import unittest
from hand import Hand

sAs2s3s4s5 = Hand([['s', '01', 0], ['s', '02', 0], ['s', '03', 0], ['s', '04', 0], ['s', '05', 0]])
sAsQsKsJsT = Hand([['s', '01', 0], ['s', '12', 0], ['s', '13', 0], ['s', '11', 0], ['s', '10', 0]])
sAhAdAcAc4 = Hand([['s', '01', 0], ['h', '01', 0], ['d', '01', 0], ['c', '01', 0], ['c', '04', 0]])
sAcAd2h2c4 = Hand([['s', '01', 0], ['c', '01', 0], ['d', '02', 0], ['h', '02', 0], ['c', '04', 0]])
sAcQsKsJsT = Hand([['s', '01', 0], ['c', '12', 0], ['s', '13', 0], ['s', '11', 0], ['s', '10', 0]])

s2s3s5sAs4 = Hand([['s', '02', 0], ['s', '03', 0], ['s', '05', 0], ['s', '01', 0], ['s', '04', 0]])
s2s3s5s6s4 = Hand([['s', '02', 0], ['s', '03', 0], ['s', '05', 0], ['s', '06', 0], ['s', '04', 0]])
s2s3d5sAc4 = Hand([['s', '02', 0], ['s', '03', 0], ['d', '05', 0], ['s', '01', 0], ['c', '04', 0]])
s2s3dKsAc4 = Hand([['s', '02', 0], ['s', '03', 0], ['d', '13', 0], ['s', '01', 0], ['c', '04', 0]])
s2c3s5hAs4 = Hand([['s', '02', 0], ['c', '03', 0], ['s', '05', 0], ['h', '01', 0], ['s', '04', 0]])
s2c3s5h6s4 = Hand([['s', '02', 0], ['c', '03', 0], ['s', '05', 0], ['h', '06', 0], ['s', '04', 0]])

s4cAdAhAc4 = Hand([['s', '04', 0], ['c', '01', 0], ['d', '01', 0], ['h', '01', 0], ['c', '04', 0]])
s4cAdAhAc5 = Hand([['s', '04', 0], ['c', '01', 0], ['d', '01', 0], ['h', '01', 0], ['c', '05', 0]])
s4cAd3h4c5 = Hand([['s', '04', 0], ['c', '01', 0], ['d', '03', 0], ['h', '04', 0], ['c', '05', 0]])

s9cQsKsJsT = Hand([['s', '09', 0], ['c', '12', 0], ['s', '13', 0], ['s', '11', 0], ['s', '10', 0]])
s9sQsKsJsT = Hand([['s', '09', 0], ['s', '12', 0], ['s', '13', 0], ['s', '11', 0], ['s', '10', 0]])

cAs2s3s4s5 = Hand([['c', '01', 0], ['s', '02', 0], ['s', '03', 0], ['s', '04', 0], ['s', '05', 0]])
c2d3s5h6h4 = Hand([['c', '02', 0], ['d', '03', 0], ['s', '05', 0], ['h', '06', 0], ['h', '04', 0]])

class HandTest(unittest.TestCase):
    def test_isFlush(self):
        self.assertEqual(map(lambda hand: hand.isFlush(), [sAs2s3s4s5, cAs2s3s4s5]), [True, False])

    def test_isAHighStraight(self):
        self.assertEqual(map(lambda hand: hand.isAHighStraight(), [sAs2s3s4s5, sAcQsKsJsT, s9cQsKsJsT]), [False, True, False])

    def test_isHighRoyal(self):
        self.assertEqual(map(lambda hand: hand.isHighRoyal(), [sAsQsKsJsT, sAcQsKsJsT, s9sQsKsJsT]), [True, False, False])

    def test_isLowStraight(self):
        self.assertEqual(map(lambda hand: hand.isLowStraight(), [sAsQsKsJsT, s9sQsKsJsT, s2s3s5s6s4, s2c3s5h6s4, s2c3s5hAs4]), [False, False, True, True, False])

    def test_isLowRoyal(self):
        self.assertEqual(map(lambda hand: hand.isLowRoyal(), [s2s3s5s6s4, c2d3s5h6h4, s2s3s5sAs4]), [True, False, False])

    def test_isStraight(self):
        self.assertTrue(s2s3d5sAc4.isStraight())
        self.assertFalse(s2s3dKsAc4.isStraight())
        hand = Hand([['s', '12', 0], ['s', '13', 0], ['d', '11', 0], ['s', '01', 0], ['c', '10', 0]])
        self.assertTrue(hand.isStraight())
        hand = Hand([['s', '07', 0], ['s', '08', 0], ['d', '11', 0], ['s', '09', 0], ['c', '10', 0]])
        self.assertTrue(hand.isStraight())
        hand = Hand([['s', '05', 0], ['s', '08', 0], ['d', '11', 0], ['s', '09', 0], ['c', '10', 0]])
        self.assertFalse(hand.isStraight())
        hand = Hand([['s', '11', 0], ['s', '08', 0], ['d', '11', 0], ['s', '09', 0], ['c', '10', 0]])
        self.assertFalse(hand.isStraight())

    def test_isStraightFlush(self):
        hand = Hand([['s', '02', 0], ['s', '03', 0], ['d', '05', 0], ['s', '01', 0], ['c', '04', 0]])
        self.assertFalse(hand.isStraightFlush())
        hand = Hand([['s', '01', 0], ['s', '12', 0], ['s', '13', 0], ['s', '11', 0], ['s', '10', 0]])
        self.assertTrue(hand.isStraightFlush())
        hand = Hand([['s', '08', 0], ['s', '12', 0], ['s', '09', 0], ['s', '11', 0], ['s', '10', 0]])
        self.assertTrue(hand.isStraightFlush())

    def test_getCountOfRank(self):
        hand = Hand([['s', '01', 0], ['c', '01', 0], ['d', '01', 0], ['h', '01', 0], ['c', '04', 0]])
        self.assertEqual(hand.getCountOfRank(), [4, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        hand = Hand([['s', '04', 0], ['c', '01', 0], ['d', '01', 0], ['h', '01', 0], ['c', '04', 0]])
        self.assertEqual(hand.getCountOfRank(), [3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def test_is4OfAKind(self):
        hand = Hand([['s', '01', 0], ['c', '01', 0], ['d', '01', 0], ['h', '01', 0], ['c', '04', 0]])
        self.assertTrue(hand.is4OfAKind())
        hand = Hand([['s', '04', 0], ['c', '01', 0], ['d', '01', 0], ['h', '01', 0], ['c', '04', 0]])
        self.assertFalse(hand.is4OfAKind())

    def test_isFullHouse(self):
        hand = Hand([['s', '01', 0], ['c', '01', 0], ['d', '01', 0], ['h', '01', 0], ['c', '04', 0]])
        self.assertFalse(hand.isFullHouse())
        hand = Hand([['s', '04', 0], ['c', '01', 0], ['d', '01', 0], ['h', '01', 0], ['c', '04', 0]])
        self.assertTrue(hand.isFullHouse())

    def test_is3OfAKind(self):
        self.assertEqual(map(lambda hand: hand.is3OfAKind(), [sAhAdAcAc4, s4cAdAhAc4, s4cAdAhAc5]), [False, False, True])

    def test_get3OfAKind(self):
        self.assertEqual(map(lambda hand: hand.get3OfAKind(), [sAhAdAcAc4, s4cAdAhAc4]), [False, False])
        self.assertCardsEqual(s4cAdAhAc5.get3OfAKind(), [['c', '01'], ['d', '01'], ['h', '01']])

    def test_is2Pair(self):
        self.assertEqual(map(lambda hand: hand.is2Pair(), [sAcAd2h2c4, s4cAdAhAc4, s4cAd3h4c5]), [True, False, False])

    def test_get2Pair(self):
        self.assertCardsEqual(sAcAd2h2c4.get2Pair(), [['s', '01'], ['c', '01'], ['d', '02'], ['h', '02']])
        self.assertEqual(map(lambda hand: hand.get2Pair(), [s4cAdAhAc4, s4cAd3h4c5]), [False, False])

    def test_is1Pair(self):
        hand = Hand([['s', '01', 0], ['c', '01', 0], ['d', '02', 0], ['h', '02', 0], ['c', '04', 0]])
        self.assertFalse(hand.is1Pair())
        hand = Hand([['s', '04', 0], ['c', '01', 0], ['d', '01', 0], ['h', '01', 0], ['c', '04', 0]])
        self.assertFalse(hand.is1Pair())
        hand = Hand([['s', '04', 0], ['c', '01', 0], ['d', '03', 0], ['h', '04', 0], ['c', '05', 0]])
        self.assertTrue(hand.is1Pair())

    def test_getCountOfSuit(self):
        hand = Hand([['s', '01', 0], ['c', '01', 0], ['d', '02', 0], ['h', '02', 0], ['c', '04', 0]])
        self.assertEqual(hand.getCountOfSuit(), [1, 1, 1, 2])
        
    def assertCardsEqual(self, cards, list):
        self.assertEqual(len(cards), len(list))
        [self.assertTrue(card.isEqual(expected[0], expected[1])) for (card, expected) in zip(cards, list)]

    def test_get4toHighRoyal(self):
        self.assertCardsEqual(sAcQsKsJsT.get4toHighRoyal(), [['s', '01'], ['s', '10'], ['s', '11'], ['s', '13']])
        self.assertFalse(cAs2s3s4s5.get4toHighRoyal())

    def test_get4toLowRoyal(self):
        self.assertFalse(sAcQsKsJsT.get4toLowRoyal())
        self.assertCardsEqual(cAs2s3s4s5.get4toLowRoyal(), [['s', '02'], ['s', '03'], ['s', '04'], ['s', '05']])
        

if __name__ == '__main__':
    unittest.main()
