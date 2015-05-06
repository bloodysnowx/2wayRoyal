from org.sikuli.basics.proxies import Vision
Vision.setParameter("MinTargetSize", 8)

# Settings.MinSimilarity = 0.99

import time

def uncheckHoldAll(region):
    while region.exists("hold.png"):
        uncheckHold(region)

def uncheckHold(region):
    region.click("hold.png")

def clickDouble(region):
    region.click("double.png")

def getWindow():
    switchApp("2 Ways Royal")
    return App.focusedWindow()

def getRegion():
    gameWindow = getWindow()
    return Region(gameWindow.getX() + gameWindow.getW() / 5, gameWindow.getY() + gameWindow.getH() / 2, gameWindow.getW() * 11 / 20, gameWindow.getH() / 4)
    
def main():
    region = getRegion()
    print(region)
    uncheckHoldAll(region)
    start = time.time()
    hand = readHand(region)
    end = time.time()
    print(start)
    print(end)
    print(end - start)
    print(hand)

def readHand(region):
    hand = []
    for suit in ["s", "h", "d", "c"]:
        for rank in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]:
            m = region.exists(suit + rank + ".png", 0.001)
            if m:
                if m.getScore() > 0.99:
                    hand.append([suit, rank, m.getTarget()])
                    if len(hand) == 5:
                        return hand
    return hand
    
main()

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

#spade
#find("s01.png"), find("s02.png"), find("s03.png"), find("s04.png"), find("s05.png"), 
#find("s06.png"), find("s07.png"), find("s08.png"), find("s09.png"), find("s10.png"), 
#find("s11.png"), find("s12.png"), find("s13.png")

#heart
#find("h01.png"), find("h02.png"), find("h03.png"), find("h04.png"), find("h05.png"),
#find("h06.png"), find("h07.png"), find("h08.png"), find("h09.png"), find("h10.png"),
#find("h11.png"), find("h12.png"), find("h13.png")


#diamond
#find("d01.png"), find("d02.png"), find("d03.png"), find("d04.png"), find("d05.png"),
#find("d06.png"), find("d07.png"), find("d08.png"), find("d09.png"), find("d10.png"),
#find("d11.png"), find("d12.png"), find("d13.png")


#club
#find("c01.png"), find("c02.png"), find("c03.png"), find("c04.png"), find("c05.png"),
#find("c06.png"), find("c07.png"), find("c08.png"), find("c09.png"), find("c10.png"),
#find("c11.png"), find("c12.png"), find("c13.png")
