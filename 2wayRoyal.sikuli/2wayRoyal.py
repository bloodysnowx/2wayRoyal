PATH = getBundlePath()
if not PATH in sys.path: sys.path.append(PATH)
execfile(PATH + 'strategy.py')
execfile(PATH + 'hand.py')

from org.sikuli.basics.proxies import Vision

def setup():
    Vision.setParameter("MinTargetSize", 8)
    Settings.MoveMouseDelay = 0

def uncheckHoldAll(region):
    while region.exists("hold.png", 0.001):
        uncheckHold(region)

def uncheckHold(region):
    region.click("hold.png")

def clickDouble(region):
    region.click("double.png")

def getWindow():
    switchApp("2 Ways Royal")
    return App.focusedWindow()

def getCardArea():
    gameWindow = getWindow()
    x = gameWindow.getX() + gameWindow.getW() / 5
    y = gameWindow.getY() + gameWindow.getH() / 2
    width = gameWindow.getW() * 11 / 20
    height = gameWindow.getH() / 4
    return Region(x, y, width, height)
    
def main():
    setup()
    # gameWindow = getWindow()
    # region = getCardArea()
    # uncheckHoldAll(region)
    # hand = readHand(region)
    strategy = Strategy()
    # holdHands = strategy.execute(hand)

def readHand(region):

    hand = []
    for suit in ["s", "h", "d", "c"]:
        for rank in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13"]:
            m = region.exists(suit + rank + ".png", 0.001)
            if m:
                if m.getScore() > 0.99:
                    hand.append([suit, rank, m.getTarget()])
                    if len(hand) == 5:
                        return Hand(hand)
    return Hand(hand)
    
main()


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
