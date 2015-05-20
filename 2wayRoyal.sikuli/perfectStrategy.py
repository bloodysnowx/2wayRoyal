class PerfectStrategy:
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
        # ex 3 to a Straight Flush: 7TJ
        ret = hand.get7TJsuited()
        if ret != False:
            return ret
        # ex 3 to a Straight Flush: 78J 	2 to a Straight: JQ 	7♣8♣J♣Q♦A♥
        ret = hand.get78Jsuited()
        if ret != False:
            return ret
        # ex 3 to a Straight Flush: 79J 	2 to a Straight: JQ 	7♣9♣J♣Q♦A♥
        ret = hand.get79Jsuited()
        if ret != False:
            return ret
        # ex 2 to a Straight(JQ)
        ret = hand.getJQ()
        if ret != False:
            return ret
        # 3 to a Straight Flush(A23; A24; A25; A34; A35; A45; 568; 578; 689; 78J; 79J; 7TJ; 89Q; 8TQ; 9TK)
        ret = hand.get3toStraightFlushD()
        if ret != False:
            return ret
        # ex 2 to a Straight: JA
        ret = hand.getJA()
        if ret != False:
            return ret
        # ex 2 to a Royal Flush: TJ
        ret = hand.getTJsuited()
        if ret != False:
            return ret
        # 2 to a Straight(JK)
        ret = hand.getJK()
        if ret != False:
            return ret
        # ex 3 to a Straight Flush(679)
        ret = hand.get679suited()
        if ret != False:
            return ret
        # 3 to a Straight Flush 	457; 467; 679; 78T; 79T
        # Single Card: a Jack 	3 to a Straight Flush: 457 	
        # Single Card: a Jack 	3 to a Straight Flush: 467 	
        # Single Card: a Jack 	3 to a Straight Flush: 78T 	
        # Single Card: a Jack 	3 to a Straight Flush: 79T 	
        if hand.get3toStraightFlushE():
            ret = hand.getSingleJack()
            if ret != False:
                return ret
            return hand.get3toStraightFlushE()
        # 2 to a Straight(JA; QK)
        ret = hand.getJAorQK()
        if ret != False:
            return ret
        # ex 2 to a Straight(KA)
        ret = hand.getKA()
        if ret != False:
            return ret
        # ex 2 to a Royal(TQ)
        ret = hand.getTQsuited()
        if ret != False:
            return ret
        ret = hand.getTKsuited()
        # ex 2 to a Straight(QA)
        ret = hand.getQA()
        if ret != False:
            return ret
        # 2 to a Royal Flush: TK
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
        # 2 to a Straight Flush: 34 	Garbage: Discard everything 	
        # 2 to a Straight Flush: 35 	Garbage: Discard everything 	
        ret = hand.get34or35suited()
        if ret != False:
            return ret

        return []



# 2 to a Straight: JK 	3 to a Straight Flush: 78J 	
# 2 to a Straight: JK 	3 to a Straight Flush: 79J 	
# 3 to a Straight Flush: 457 	2 to a Straight: JK 	4♣5♣7♣J♦K♥
# 3 to a Straight Flush: 467 	2 to a Straight: JK 	4♣6♣7♣J♦K♥
# 3 to a Straight Flush: 679 	2 to a Straight: JK 	6♣7♣9♣J♦K♥
# Single Card: a Jack 	3 to a Straight Flush: 568 	4♣5♦6♦8♦J♥
# Single Card: a Jack 	3 to a Straight Flush: 578 	4♣5♦7♦8♦J♥
# 3 to a Straight Flush: 789 	2 to a Royal Flush: QK 	7♣8♣9♣Q♦K♦
# 3 to a Straight Flush: 567 	2 to a Royal Flush: JA 	5♣6♣7♣J♦A♦
# 3 to a Straight Flush: 678 	2 to a Royal Flush: JA 	6♣7♣8♣J♦A♦
