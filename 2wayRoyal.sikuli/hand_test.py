import unittest
from hand import Hand

cAs2s3s4s5 = Hand([['c', '01', 0], ['s', '02', 0], ['s', '03', 0], ['s', '04', 0], ['s', '05', 0]])
sAs2s3s4s5 = Hand([['s', '01', 0], ['s', '02', 0], ['s', '03', 0], ['s', '04', 0], ['s', '05', 0]])
sAcQsKsJsT = Hand([['s', '01', 0], ['c', '12', 0], ['s', '13', 0], ['s', '11', 0], ['s', '10', 0]])
sAsQsKsJsT = Hand([['s', '01', 0], ['s', '12', 0], ['s', '13', 0], ['s', '11', 0], ['s', '10', 0]])
s9cQsKsJsT = Hand([['s', '09', 0], ['c', '12', 0], ['s', '13', 0], ['s', '11', 0], ['s', '10', 0]])
s9sQsKsJsT = Hand([['s', '09', 0], ['s', '12', 0], ['s', '13', 0], ['s', '11', 0], ['s', '10', 0]])

class HandTest(unittest.TestCase):
    def test_isFlush(self):
        self.assertEqual(map(lambda hand: hand.isFlush(), [sAs2s3s4s5, cAs2s3s4s5]), [True, False])

    def test_isAHighStraight(self):
        self.assertEqual(map(lambda hand: hand.isAHighStraight(), [sAs2s3s4s5, sAcQsKsJsT, s9cQsKsJsT]), [False, True, False])

    def test_isHighRoyal(self):
        self.assertEqual(map(lambda hand: hand.isHighRoyal(), [sAsQsKsJsT, sAcQsKsJsT, s9sQsKsJsT]), [True, False, False])

    def test_isLowStraight(self):
        hand = Hand([['s', '01', 0], ['s', '12', 0], ['s', '13', 0], ['s', '11', 0], ['s', '10', 0]])
        self.assertFalse(hand.isLowStraight())
        hand = Hand([['s', '09', 0], ['s', '12', 0], ['s', '13', 0], ['s', '11', 0], ['s', '10', 0]])
        self.assertFalse(hand.isLowStraight())
        hand = Hand([['s', '02', 0], ['s', '03', 0], ['s', '05', 0], ['s', '06', 0], ['s', '04', 0]])
        self.assertTrue(hand.isLowStraight())
        hand = Hand([['s', '02', 0], ['c', '03', 0], ['s', '05', 0], ['h', '06', 0], ['s', '04', 0]])
        self.assertTrue(hand.isLowStraight())
        hand = Hand([['s', '02', 0], ['c', '03', 0], ['s', '05', 0], ['h', '01', 0], ['s', '04', 0]])
        self.assertFalse(hand.isLowStraight())

    def test_isLowRoyal(self):
        hand = Hand([['s', '02', 0], ['s', '03', 0], ['s', '05', 0], ['s', '06', 0], ['s', '04', 0]])
        self.assertTrue(hand.isLowRoyal())
        hand = Hand([['c', '02', 0], ['d', '03', 0], ['s', '05', 0], ['h', '06', 0], ['h', '04', 0]])
        self.assertFalse(hand.isLowRoyal())
        hand = Hand([['s', '02', 0], ['s', '03', 0], ['s', '05', 0], ['s', '01', 0], ['s', '04', 0]])
        self.assertFalse(hand.isLowRoyal())

    def test_isStraight(self):
        hand = Hand([['s', '02', 0], ['s', '03', 0], ['d', '05', 0], ['s', '01', 0], ['c', '04', 0]])
        self.assertTrue(hand.isStraight())
        hand = Hand([['s', '02', 0], ['s', '03', 0], ['d', '13', 0], ['s', '01', 0], ['c', '04', 0]])
        self.assertFalse(hand.isStraight())
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
        hand = Hand([['s', '01', 0], ['c', '01', 0], ['d', '01', 0], ['h', '01', 0], ['c', '04', 0]])
        self.assertFalse(hand.is3OfAKind())
        hand = Hand([['s', '04', 0], ['c', '01', 0], ['d', '01', 0], ['h', '01', 0], ['c', '04', 0]])
        self.assertFalse(hand.is3OfAKind())
        hand = Hand([['s', '04', 0], ['c', '01', 0], ['d', '01', 0], ['h', '01', 0], ['c', '05', 0]])
        self.assertTrue(hand.is3OfAKind())

    def test_is2Pair(self):
        hand = Hand([['s', '01', 0], ['c', '01', 0], ['d', '02', 0], ['h', '02', 0], ['c', '04', 0]])
        self.assertTrue(hand.is2Pair())
        hand = Hand([['s', '04', 0], ['c', '01', 0], ['d', '01', 0], ['h', '01', 0], ['c', '04', 0]])
        self.assertFalse(hand.is2Pair())
        hand = Hand([['s', '04', 0], ['c', '01', 0], ['d', '03', 0], ['h', '04', 0], ['c', '05', 0]])
        self.assertFalse(hand.is2Pair())

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

if __name__ == '__main__':
    unittest.main()
