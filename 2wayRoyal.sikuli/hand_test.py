import unittest
from hand import Hand

class HandTest(unittest.TestCase):
    def test_isFlush(self):
        hand = Hand([['s', '01', 0], ['s', '02', 0], ['s', '03', 0], ['s', '04', 0], ['s', '05', 0]])
        self.assertEqual(True, hand.isFlush())
        hand = Hand([['c', '01', 0], ['s', '02', 0], ['s', '03', 0], ['s', '04', 0], ['s', '05', 0]])
        self.assertEqual(False, hand.isFlush())

if __name__ == '__main__':
    unittest.main()
