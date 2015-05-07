import unittest
from hand import Hand

class HandTest(unittest.TestCase):
    def test_isFlush(self):
        hand = Hand([['s', '01', 0], ['s', '02', 0], ['s', '03', 0], ['s', '04', 0], ['s', '05', 0]])
        self.assertTrue(hand.isFlush())
        hand = Hand([['c', '01', 0], ['s', '02', 0], ['s', '03', 0], ['s', '04', 0], ['s', '05', 0]])
        self.assertFalse(hand.isFlush())

    def test_isAHighStraight(self):
        hand = Hand([['s', '01', 0], ['s', '02', 0], ['s', '03', 0], ['s', '04', 0], ['s', '05', 0]])
        self.assertFalse(hand.isAHighStraight())
        hand = Hand([['s', '01', 0], ['c', '12', 0], ['s', '13', 0], ['s', '11', 0], ['s', '10', 0]])
        self.assertTrue(hand.isAHighStraight())
        hand = Hand([['s', '09', 0], ['c', '12', 0], ['s', '13', 0], ['s', '11', 0], ['s', '10', 0]])
        self.assertFalse(hand.isAHighStraight())

    def test_isHighRoyal(self):
        hand = Hand([['s', '01', 0], ['s', '12', 0], ['s', '13', 0], ['s', '11', 0], ['s', '10', 0]])
        self.assertTrue(hand.isHighRoyal())
        hand = Hand([['s', '01', 0], ['s', '12', 0], ['h', '13', 0], ['s', '11', 0], ['s', '10', 0]])
        self.assertFalse(hand.isHighRoyal())
        hand = Hand([['s', '09', 0], ['s', '12', 0], ['s', '13', 0], ['s', '11', 0], ['s', '10', 0]])
        self.assertFalse(hand.isHighRoyal())

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




if __name__ == '__main__':
    unittest.main()
