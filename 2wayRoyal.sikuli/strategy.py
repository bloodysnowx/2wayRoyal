class Strategy:
    def execute(hand):
        return True
    
# High Royal -> Pat
# Low Royal -> Pat
# Straight Flush -> Pat
# 4 of a Kind -> Pat
# Full House -> Pat
# 4 to a Royal(TJQA,  TJQK, TJKA, TQKA JQKA) -> Hold 4
# 4 to a Low Royal(2345, 2346, 2356, 2456, 3456) -> Hold 4
# Flush -> Pat
# Straight -> Pat
# 3 of a Kind -> Hold 3
# 2 Pair -> Hold 4
# 4 to a Straight Flush -> Hold 4
# 1 Pair(JJ-AA) -> Hold 2
# 3 to a Royal(TJA, TJQ, TJK, TQA, TQK, TKA, JQA, JQK, JKA, QKA) -> Hold 3
# 3 to a Low Royal
# 4 to a Flush
# 4 to a Straight(TJQK)
# 1 Pair(22-TT)
# 4 to a Straight(2345-9TJQ)
# 3 to a Straight Flush(89J; 8TJ; 8JQ; 9TJ; 9TQ; 9JQ)
# 4 to a Straight(JQKA)
# 3 to a Straight Flush(9JK; 9QK)
# 2 to a Royal(JA; JQ; JK; QK)
# 3 to a Straight Flush(567; 678; 789; 89T)
# 2 to a Royal(QA; KA)
# 4 to a Straight(9JQK; TJQA; TJKA; TQKA)
# 3 to a Straight(JQK)
# 2 to a Straight(JQ)
# 3 to a Straight Flush(A23; A24; A25; A34; A35; A45; 568; 578; 689; 78J; 79J; 7TJ; 89Q; 8TQ; 9TK)
# ex 2 to a Royal(TJ)
# 2 to a Straight(JK)
# 2 to a Royal(TJ)
# 3 to a Straight Flush(457; 467; 679; 78T; 79T)
# 2 to a Straight(JA; QK)
# 2 to a Straight(KA)
# ex 2 to Royal(TQ)
# 2 to a Straight(QA)
# 2 to a Royal(TQ)
# ex 2 to a Royal(TK)
# Single Card(J-A)
# 3 to a Straight Flush(347; 357; 367; 458; 468; 478; 569; 579; 589; 67T; 68T; 69T)
# ex Garbage Discard everything
# 2 to a Straight Flush(45; 56)
# Garbage Discard everything
