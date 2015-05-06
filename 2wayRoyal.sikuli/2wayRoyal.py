def uncheckHoldAll():
    while exists("hold.png"):
        uncheckHold()

find("double.png")

def uncheckHold():
    click("hold.png")

def main():
    uncheckHoldAll()

main()

#spade
find("s01.png"), find("s02.png"), find("s03.png"), find("s04.png"), find("s05.png"), 
find("s06.png"), find("s07.png"), find("s08.png"), find("s09.png"), find("s10.png"), 
find("s11.png"), find("s12.png"), find("s13.png")

#heart
find("h01.png"), find("h02.png"), find("h03.png"), find("h04.png"), find("h05.png"),
find("h06.png"), find("h07.png"), find("h08.png"), find("h09.png"), find("h10.png"),
find("h11.png"), find("h12.png"), find("h13.png")


#diamond
find("d01.png"), find("d02.png"), find("d03.png"), find("d04.png"), find("d05.png"),
find("d06.png"), find("d07.png"), find("d08.png"), find("d09.png"), find("d10.png"),
find("d11.png"), find("d12.png"), find("d13.png")


#club
find("c01.png"), find("c02.png"), find("c03.png"), find("c04.png"), find("c05.png"),
find("c06.png"), find("c07.png"), find("c08.png"), find("c09.png"), find("c10.png"),
find("c11.png"), find("c12.png"), find("c13.png")
