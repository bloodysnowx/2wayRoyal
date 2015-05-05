def uncheckHoldAll():
    while exists("hold.png"):
        uncheckHold()

def uncheckHold():
    click("hold.png")

def main():
    uncheckHoldAll()

main()
