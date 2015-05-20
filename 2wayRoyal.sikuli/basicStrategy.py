class BasicStrategy:
    def execute(self, hand):
        # High Royal -> Pat
        if hand.isHighRoyal():
            return hand.cards
        # Low Royal -> Pat
        if hand.isLowRoyal():
            return hand.cards
        # Straight Flush -> Pat
        if hand.isStraightFlush():
            return hand.cards
        # 4 of a Kind -> Pat
        if hand.is4OfAKind():
            return hand.cards
        # Full House -> Pat
        if hand.isFullHouse():
            return hand.cards
        # 4 to a Royal(TJQA,  TJQK, TJKA, TQKA JQKA) -> Hold 4
        ret = hand.get4toHighRoyal()
        if ret != False:
            return ret
        # 4 to a Low Royal(2345, 2346, 2356, 2456, 3456) -> Hold 4
        ret = hand.get4toLowRoyal()
        if ret != False:
            return ret
        # Flush -> Pat
        if hand.isFlush():
            return hand.cards
        # Straight -> Pat
        if hand.isStraight():
            return hand.cards
        # 3 of a Kind -> Hold 3
        ret = hand.get3OfAKind()
        if ret != False:
            return ret
        # 2 Pair -> Hold 4
        ret = hand.get2Pair()
        if ret != False:
            return ret
        # 4 to a Straight Flush -> Hold 4
        ret = hand.get4toStraightFlush()
        if ret != False:
            return ret
        # 1 Pair(JJ-AA) -> Hold 2
        if hand.isJackOrBetter():
            return hand.get1Pair()
        # 3 to a Royal(TJA, TJQ, TJK, TQA, TQK, TKA, JQA, JQK, JKA, QKA) -> Hold 3
        ret = hand.get3toHighRoyal()
        if ret != False:
            return ret
        # 3 to a Low Royal
        ret = hand.get3toLowRoyal()
        if ret != False:
            return ret
        # 4 to a Flush
        ret = hand.get4toFlush()
        if ret != False:
            return ret
        # 4 to a Straight(TJQK)
        ret = hand.getTJQK()
        if ret != False:
            return ret
        # 1 Pair(22-TT)
        if hand.is1Pair():
            return hand.get1Pair()
        # 4 to a Straight(2345-9TJQ)
        ret = hand.getOESD()
        if hand.is1Pair():
            return hand.get1Pair()
        # 3 to a Straight Flush(89J; 8TJ; 8JQ; 9TJ; 9TQ; 9JQ)
        ret = hand.get3toStraightFlushA()
        if ret != False:
            return ret
        # 4 to a Straight(JQKA)
        ret = hand.getJQKA()
        if ret != False:
            return ret                
        # 3 to a Straight Flush(9JK; 9QK)
        ret = hand.get3toStraightFlushB()
        if ret != False:
            return ret
        # 2 to a Royal(JA; JQ; JK; QK)
        ret = hand.get2toHighRoyalA()
        if ret != False:
            return ret
        # 3 to a Straight Flush(567; 678; 789; 89T)
        ret = hand.get3toStraightFlushC()
        if ret != False:
            return ret
        # 2 to a Royal(QA; KA)
        ret = hand.get2toHighRoyalA()
        if ret != False:
            return ret
        # 4 to a Straight(9JQK; TJQA; TJKA; TQKA)
        ret = hand.get4toStraightA()
        if ret != False:
            return ret
        # 3 to a Straight(JQK)
        ret = hand.getJQK()
        if ret != False:
            return ret
        # 2 to a Straight(JQ)
        ret = hand.getJQ()
        if ret != False:
            return ret
        # 3 to a Straight Flush(A23; A24; A25; A34; A35; A45; 568; 578; 689; 78J; 79J; 7TJ; 89Q; 8TQ; 9TK)
        ret = hand.get3toStraightFlushD()
        if ret != False:
            return ret
        # 2 to a Straight(JK)
        ret = hand.getJK()
        if ret != False:
            return ret
        # 2 to a Royal(TJ)
        ret = hand.getTJsuited()
        if ret != False:
            return ret
        # 3 to a Straight Flush(457; 467; 679; 78T; 79T)
        ret = hand.get3toStraightFlushE()
        if ret != False:
            return ret
        # 2 to a Straight(JA; QK)
        ret = hand.getJAorQK()
        if ret != False:
            return ret
        # 2 to a Straight(KA), 2 to a Straight(QA)
        ret = hand.getQAorKA()
        if ret != False:
            return ret
        # 2 to a Royal(TQ)
        ret = hand.getTQsuited()
        if ret != False:
            return ret
        # Single Card(J-A)
        ret = hand.getSingleJackOrBetter()
        if ret != False:
            return ret
        # 3 to a Straight Flush(347; 357; 367; 458; 468; 478; 569; 579; 589; 67T; 68T; 69T)
        ret = hand.get3toStraightFlushF()
        if ret != False:
            return ret
        # 2 to a Straight Flush(45; 56)
        ret = hand.get45or56suited()
        if ret != False:
            return ret

        return []
