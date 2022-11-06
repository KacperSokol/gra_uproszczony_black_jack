import random
import curses
serce="♥"
pik="♠"
trefl="♣"
romb="♦"
screen = curses.initscr()
curses.start_color()
curses.use_default_colors()
curses.init_pair(1, 9, -1)
curses.init_pair(2, 47, -1)

def rysujWygrana1():
    screen.addstr(34, 4, " .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.   .----------------. ",2)
    screen.addstr(35, 4, "| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. |",2)
    screen.addstr(36, 4, "| | _____  _____ | || |  ____  ____  | || |    ______    | || |  _______     | || |      __      | || | ____  _____  | || |      __      | | | |     __       | |",2)
    screen.addstr(37, 4, "| ||_   _||_   _|| || | |_  _||_  _| | || |  .' ___  |   | || | |_   __ \    | || |     /  \     | || ||_   \|_   _| | || |     /  \     | | | |    /  |      | |",2)
    screen.addstr(38, 4, "| |  | | /\ | |  | || |   \ \  / /   | || | / .'   \_|   | || |   | |__) |   | || |    / /\ \    | || |  |   \ | |   | || |    / /\ \    | | | |    `| |      | |",2)
    screen.addstr(39, 4, "| |  | |/  \| |  | || |    \ \/ /    | || | | |    ____  | || |   |  __ /    | || |   / ____ \   | || |  | |\ \| |   | || |   / ____ \   | | | |     | |      | |",2)
    screen.addstr(40, 4, "| |  |   /\   |  | || |    _|  |_    | || | \ `.___]  _| | || |  _| |  \ \_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | _/ /    \ \_ | | | |    _| |_     | |",2)
    screen.addstr(41, 4, "| |  |__/  \__|  | || |   |______|   | || |  `._____.'   | || | |____| |___| | || ||____|  |____|| || ||_____|\____| | || ||____|  |____|| | | |   |_____|    | |",2)
    screen.addstr(42, 4, "| |              | || |              | || |              | || |              | || |              | || |              | || |              | | | |              | |",2)
    screen.addstr(43, 4, "| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' |",2)
    screen.addstr(44, 4, " '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   '----------------' ",2)
def rysujWygrana2():
    screen.addstr(34, 4, " .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.   .----------------. ",2)
    screen.addstr(35, 4, "| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. | | .--------------. |",2)
    screen.addstr(36, 4, "| | _____  _____ | || |  ____  ____  | || |    ______    | || |  _______     | || |      __      | || | ____  _____  | || |      __      | | | |    _____     | |",2)
    screen.addstr(37, 4, "| ||_   _||_   _|| || | |_  _||_  _| | || |  .' ___  |   | || | |_   __ \    | || |     /  \     | || ||_   \|_   _| | || |     /  \     | | | |   / ___ `.   | |",2)
    screen.addstr(38, 4, "| |  | | /\ | |  | || |   \ \  / /   | || | / .'   \_|   | || |   | |__) |   | || |    / /\ \    | || |  |   \ | |   | || |    / /\ \    | | | |  |_/___) |   | |",2)
    screen.addstr(39, 4, "| |  | |/  \| |  | || |    \ \/ /    | || | | |    ____  | || |   |  __ /    | || |   / ____ \   | || |  | |\ \| |   | || |   / ____ \   | | | |   .'____.'   | |",2)
    screen.addstr(40, 4, "| |  |   /\   |  | || |    _|  |_    | || | \ `.___]  _| | || |  _| |  \ \_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | _/ /    \ \_ | | | |  / /____     | |",2)
    screen.addstr(41, 4, "| |  |__/  \__|  | || |   |______|   | || |  `._____.'   | || | |____| |___| | || ||____|  |____|| || ||_____|\____| | || ||____|  |____|| | | |  |_______|   | |",2)
    screen.addstr(42, 4, "| |              | || |              | || |              | || |              | || |              | || |              | || |              | | | |              | |",2)
    screen.addstr(43, 4, "| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' | | '--------------' |",2)
    screen.addstr(44, 4, " '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   '----------------' ",2)
#wymiar karty 12x9
def rysujKarte(karta,X,Y):
    if karta[1:] == "1":
        wartosc = "A"
    elif karta[1:] == "11":
        wartosc = "J"
    elif karta[1:] == "12":
        wartosc = "Q"
    elif karta[1:] == "13":
        wartosc = "K"
    else:
        wartosc = karta[1:]
    symbol=karta[0]
    if symbol==pik or symbol==trefl:
        screen.addstr(X, Y, "╔══════════╗")
        screen.addstr(X+1, Y, "║ "+symbol+"        ║")
        if wartosc=="10":
            screen.addstr(X+2, Y, "║ " + wartosc + "       ║")
        else:
            screen.addstr(X + 2, Y, "║ " + wartosc + "        ║")
        for i in range(3):
            screen.addstr(i+3+X, Y, "║          ║")
        if wartosc == "10":
            screen.addstr(X+6, Y, "║       " + wartosc + " ║")
        else:
            screen.addstr(X + 6, Y, "║        " + wartosc + " ║")
        screen.addstr(X+7, Y, "║        "+symbol+" ║")
        screen.addstr(X+8, Y, "╚══════════╝")
    else:
        screen.addstr(X, Y, "╔══════════╗", curses.color_pair(1))
        screen.addstr(X+1, Y, "║ "+symbol+"        ║", curses.color_pair(1))
        if wartosc=="10":
            screen.addstr(X+2, Y, "║ " + wartosc + "       ║", curses.color_pair(1))
        else:
            screen.addstr(X + 2, Y, "║ " + wartosc + "        ║", curses.color_pair(1))
        for i in range(3):
            screen.addstr(i+3+X, Y, "║          ║", curses.color_pair(1))
        if wartosc == "10":
            screen.addstr(X+6, Y, "║       " + wartosc + " ║", curses.color_pair(1))
        else:
            screen.addstr(X + 6, Y, "║        " + wartosc + " ║", curses.color_pair(1))
        screen.addstr(X+7, Y, "║        "+symbol+" ║", curses.color_pair(1))
        screen.addstr(X+8, Y, "╚══════════╝", curses.color_pair(1))

screen.border(0)
screen.refresh()

karty=["♥1","♥2","♥3","♥4","♥5","♥6","♥7","♥8","♥9","♥10","♥11","♥12","♥13",
       "♠1","♠2","♠3","♠4","♠5","♠6","♠7","♠8","♠9","♠10","♠11","♠12","♠13",
       "♣1","♣2","♣3","♣4","♣5","♣6","♣7","♣8","♣9","♣10","♣11","♣12","♣13",
       "♦1","♦2","♦3","♦4","♦5","♦6","♦7","♦8","♦9","♦10","♦11","♦12","♦13"]
random.shuffle(karty)
def decyduj(suma):
    brakujace=21-suma
    if suma>=15:
        return 0
    else:
        return 1
kartyMoje=[]
kartyPrzeciwnika=[]

def rysujBlackJack(x,y):
    screen.addstr(y,x,"  ____  _            _           _            _ ")
    screen.addstr(y+1, x, " |  _ \| |          | |         | |          | | ")
    screen.addstr(y+2, x, " | |_) | | __ _  ___| | __      | | __ _  ___| | __ ")
    screen.addstr(y+3, x, " |  _ <| |/ _` |/ __| |/ /  _   | |/ _` |/ __| |/ / ")
    screen.addstr(y+4, x, " | |_) | | (_| | (__|   <  | |__| | (_| | (__|   < ")
    screen.addstr(y+5, x, " |____/|_|\__,_|\___|_|\_\  \____/ \__,_|\___|_|\_\ ")
def rysujWygrana():
    screen.addstr(34, 4, " .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------. ", curses.color_pair(2))
    screen.addstr(35, 4, "| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |", curses.color_pair(2))
    screen.addstr(36, 4, "| | _____  _____ | || |  ____  ____  | || |    ______    | || |  _______     | || |      __      | || | ____  _____  | || |      __      | |", curses.color_pair(2))
    screen.addstr(37, 4, "| ||_   _||_   _|| || | |_  _||_  _| | || |  .' ___  |   | || | |_   __ \    | || |     /  \     | || ||_   \|_   _| | || |     /  \     | |", curses.color_pair(2))
    screen.addstr(38, 4, "| |  | | /\ | |  | || |   \ \  / /   | || | / .'   \_|   | || |   | |__) |   | || |    / /\ \    | || |  |   \ | |   | || |    / /\ \    | |", curses.color_pair(2))
    screen.addstr(39, 4, "| |  | |/  \| |  | || |    \ \/ /    | || | | |    ____  | || |   |  __ /    | || |   / ____ \   | || |  | |\ \| |   | || |   / ____ \   | |", curses.color_pair(2))
    screen.addstr(40, 4, "| |  |   /\   |  | || |    _|  |_    | || | \ `.___]  _| | || |  _| |  \ \_  | || | _/ /    \ \_ | || | _| |_\   |_  | || | _/ /    \ \_ | |", curses.color_pair(2))
    screen.addstr(41, 4, "| |  |__/  \__|  | || |   |______|   | || |  `._____.'   | || | |____| |___| | || ||____|  |____|| || ||_____|\____| | || ||____|  |____|| |", curses.color_pair(2))
    screen.addstr(42, 4, "| |              | || |              | || |              | || |              | || |              | || |              | || |              | |", curses.color_pair(2))
    screen.addstr(43, 4, "| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |", curses.color_pair(2))
    screen.addstr(44, 4, " '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ", curses.color_pair(2))
def rysujPorazka():
    screen.addstr(34,4," .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ", curses.color_pair(1))
    screen.addstr(35,4,"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |", curses.color_pair(1))
    screen.addstr(36,4,"| |   ______     | || |     ____     | || |  _______     | || |      __      | || |   ________   | || |  ___  ____   | || |      __      | |", curses.color_pair(1))
    screen.addstr(37,4,"| |  |_   __ \   | || |   .'    `.   | || | |_   __ \    | || |     /  \     | || |  |  __   _|  | || | |_  ||_  _|  | || |     /  \     | |", curses.color_pair(1))
    screen.addstr(38,4,"| |    | |__) |  | || |  /  .--.  \  | || |   | |__) |   | || |    / /\ \    | || |  |_/  / /    | || |   | |_/ /    | || |    / /\ \    | |", curses.color_pair(1))
    screen.addstr(39,4,"| |    |  ___/   | || |  | |    | |  | || |   |  __ /    | || |   / ____ \   | || |     .'.' _   | || |   |  __'.    | || |   / ____ \   | |", curses.color_pair(1))
    screen.addstr(40,4,"| |   _| |_      | || |  \  `--'  /  | || |  _| |  \ \_  | || | _/ /    \ \_ | || |   _/ /__/ |  | || |  _| |  \ \_  | || | _/ /    \ \_ | |", curses.color_pair(1))
    screen.addstr(41,4,"| |  |_____|     | || |   `.____.'   | || | |____| |___| | || ||____|  |____|| || |  |________|  | || | |____||____| | || ||____|  |____|| |", curses.color_pair(1))
    screen.addstr(42,4,"| |              | || |              | || |              | || |              | || |              | || |              | || |              | |", curses.color_pair(1))
    screen.addstr(43,4,"| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |", curses.color_pair(1))
    screen.addstr(44,4," '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ", curses.color_pair(1))
def rysujRemis():
    screen.addstr(34,4," .----------------.  .----------------.  .----------------.  .----------------.  .----------------. ")
    screen.addstr(35,4,"| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
    screen.addstr(36,4,"| |  _______     | || |  _________   | || | ____    ____ | || |     _____    | || |    _______   | |")
    screen.addstr(37,4,"| | |_   __ \    | || | |_   ___  |  | || ||_   \  /   _|| || |    |_   _|   | || |   /  ___  |  | |")
    screen.addstr(38,4,"| |   | |__) |   | || |   | |_  \_|  | || |  |   \/   |  | || |      | |     | || |  |  (__ \_|  | |")
    screen.addstr(39,4,"| |   |  __ /    | || |   |  _|  _   | || |  | |\  /| |  | || |      | |     | || |   '.___`-.   | |")
    screen.addstr(40,4,"| |  _| |  \ \_  | || |  _| |___/ |  | || | _| |_\/_| |_ | || |     _| |_    | || |  |`\____) |  | |")
    screen.addstr(41,4,"| | |____| |___| | || | |_________|  | || ||_____||_____|| || |    |_____|   | || |  |_______.'  | |")
    screen.addstr(42,4,"| |              | || |              | || |              | || |              | || |              | |")
    screen.addstr(43,4,"| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
    screen.addstr(44,4," '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ")

opcja=1
rysujBlackJack(50,25)
screen.addstr(33,64,">>> Gra z komputerem <<<")
screen.addstr(35,70,"    1 vs 1    ")
screen.addstr(40,70,"Nawigacja w, s")
screen.addstr(42,70,"Zatwierdzenie z")
screen.addstr(0,0,"")
przycisk=screen.getch()
while(przycisk!=ord("z")):
    if przycisk==ord("w"):
        if opcja==2:
            opcja=1
    if przycisk==ord("s"):
        if opcja==1:
            opcja=2
    if opcja==1:
        screen.addstr(33,64,">>> Gra z komputerem <<<")
        screen.addstr(35,70,"    1 vs 1    ")
    else:
        screen.addstr(33, 64, "    Gra z komputerem    ")
        screen.addstr(35,70,">>> 1 vs 1 <<<")
    screen.addstr(0,0,"")
    przycisk = screen.getch()
screen.clear()
screen.border(0)
#gra z komputerem
if opcja==1:
    while(True):
        karty = ["♥1", "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥11", "♥12", "♥13",
                 "♠1", "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠11", "♠12", "♠13",
                 "♣1", "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣11", "♣12", "♣13",
                 "♦1", "♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦11", "♦12", "♦13"]
        random.shuffle(karty)
        screen.border(0)
        rysujBlackJack(50,2)
        kartyMoje = []
        kartyPrzeciwnika = []
        sumaMoja = 0
        sumaPrzeciwnika = 0
        wynik = 2
        flagaMoja=False
        flagaPrzeciwnika=False
        pozycjaMojejKartyX=1
        pozycjaPrzeciwnikaKartyX = 1
        screen.addstr(21, 10, "h - hit, s - stand")
        screen.addstr(22, 10, "Suma moja: " + str(sumaMoja) + " ")
        screen.addstr(20, 10, "Suma przeciwnika: " + str(sumaPrzeciwnika) + " ")
        while (flagaMoja==False or flagaPrzeciwnika==False):
            if not flagaMoja:
                screen.addstr(0,0,"")
                przycisk = screen.getch()  # "Podaj przycisk "
                if przycisk==ord("h"):
                    kartyMoje=karty[0]
                    karta=karty[0]
                    sumaMoja +=int(karty[0][1:])
                    karty.remove(karty[0])
                    rysujKarte(karta,24,pozycjaMojejKartyX)
                    pozycjaMojejKartyX+=14
                    screen.addstr(22, 10, "Suma moja: " + str(sumaMoja) + " ")
                elif przycisk==ord("s"):
                    flagaMoja=True
                elif not flagaMoja:
                    screen.addstr(0, 0, "")
                    przycisk = screen.getch()
            if decyduj(sumaPrzeciwnika):
                kartyPrzeciwnika=karty[0]
                karta=karty[0]
                sumaPrzeciwnika += int(karty[0][1:])
                karty.remove(karty[0])
                rysujKarte(karta,10,pozycjaPrzeciwnikaKartyX)
                pozycjaPrzeciwnikaKartyX+=14
                screen.addstr(20, 10, "Suma przeciwnika: " + str(sumaPrzeciwnika) + " ")
            else:
                flagaPrzeciwnika=True
            if sumaMoja>21 and sumaPrzeciwnika>21:
                wynik=0
                flagaMoja=True
                flagaPrzeciwnika=True
            elif sumaMoja>21:
                wynik=-1
                flagaMoja = True
                flagaPrzeciwnika = True
            elif sumaPrzeciwnika>21:
                wynik = 1
                flagaMoja = True
                flagaPrzeciwnika = True

        if wynik==2:
            if (21-sumaMoja)<(21-sumaPrzeciwnika):
                wynik=1
            elif (21-sumaMoja)>(21-sumaPrzeciwnika):
                wynik=-1
            else:
                wynik=0
        screen.refresh()
        #screen.addstr(12,10,"Wynik: "+wynik)
        if wynik==1:
            rysujWygrana()
        elif wynik==-1:
            rysujPorazka()
        else:
            rysujRemis()
        screen.addstr(46,20," ___                 _                                _    _           _  _")
        screen.addstr(47, 20, "|   \ _____ __ _____| |_ _ _  _   _ __ _ _ ____  _ __(_)__| |__  ___  | \| |_____ __ ____ _   __ _ _ _ __ _")
        screen.addstr(48, 20, "| |) / _ \ V  V / _ \ | ' \ || | | '_ \ '_|_ / || / _| (_-< / / |___| | .` / _ \ V  V / _` | / _` | '_/ _` |")
        screen.addstr(49, 20, "|___/\___/\_/\_/\___/_|_||_\_, | | .__/_| /__|\_, \__|_/__/_\_\       |_|\_\___/\_/\_/\__,_| \__, |_| \__,_|")
        screen.addstr(50, 20, "                           |__/  |_|          |__/                                           |___/")
        screen.addstr(51,20, " ____        ____         _")
        screen.addstr(52, 20, "|_  /  ___  |_  /  __ _  | |__  ___   _ _    __   ___")
        screen.addstr(53, 20, " / /  |___|  / /  / _` | | / / / _ \ | ' \  / _| |_ /")
        screen.addstr(54, 20, "/___|       /___| \__,_| |_\_\ \___/ |_||_| \__| /__|")
        screen.refresh()
        screen.addstr(0, 0, "")
        przycisk = screen.getch()  # "Podaj przycisk "
        if przycisk == ord("z"):
            break
        screen.clear()
#gra 1vs1
if opcja==2:
    while(True):
        karty = ["♥1", "♥2", "♥3", "♥4", "♥5", "♥6", "♥7", "♥8", "♥9", "♥10", "♥11", "♥12", "♥13",
                 "♠1", "♠2", "♠3", "♠4", "♠5", "♠6", "♠7", "♠8", "♠9", "♠10", "♠11", "♠12", "♠13",
                 "♣1", "♣2", "♣3", "♣4", "♣5", "♣6", "♣7", "♣8", "♣9", "♣10", "♣11", "♣12", "♣13",
                 "♦1", "♦2", "♦3", "♦4", "♦5", "♦6", "♦7", "♦8", "♦9", "♦10", "♦11", "♦12", "♦13"]
        random.shuffle(karty)
        rysujBlackJack(50,2)
        screen.border(0)
        kartyMoje = []
        kartyPrzeciwnika = []
        sumaMoja = 0
        sumaPrzeciwnika = 0
        wynik = 2
        flagaMoja=False
        flagaPrzeciwnika=False
        pozycjaMojejKartyX=1
        pozycjaPrzeciwnikaKartyX = 1
        screen.addstr(21, 10, "1 gracz: h - hit, s - stand     2 gracz: p - hit, o - stand")
        screen.addstr(22, 10, "Suma moja: " + str(sumaMoja) + " ")
        screen.addstr(20, 10, "Suma przeciwnika: " + str(sumaPrzeciwnika) + " ")
        while (flagaMoja==False or flagaPrzeciwnika==False):
            screen.addstr(0, 0, "")
            przycisk = screen.getch()
            if not flagaMoja:
                if przycisk==ord("h"):
                    kartyMoje=karty[0]
                    karta=karty[0]
                    sumaMoja +=int(karty[0][1:])
                    karty.remove(karty[0])
                    rysujKarte(karta,24,pozycjaMojejKartyX)
                    pozycjaMojejKartyX+=14
                    screen.addstr(22, 10, "Suma moja: " + str(sumaMoja) + " ")
                elif przycisk==ord("s"):
                    flagaMoja=True
            if not flagaPrzeciwnika:
                if przycisk==ord("p"):
                    kartyPrzeciwnika=karty[0]
                    karta=karty[0]
                    sumaPrzeciwnika +=int(karty[0][1:])
                    karty.remove(karty[0])
                    rysujKarte(karta,10,pozycjaPrzeciwnikaKartyX)
                    pozycjaPrzeciwnikaKartyX+=14
                    screen.addstr(20, 10, "Suma przeciwnika: " + str(sumaPrzeciwnika) + " ")
                elif przycisk==ord("o"):
                    flagaPrzeciwnika=True
            if sumaMoja>21 and sumaPrzeciwnika>21:
                wynik=0
                flagaMoja=True
                flagaPrzeciwnika=True
            elif sumaMoja>21:
                wynik=-1
                flagaMoja = True
                flagaPrzeciwnika = True
            elif sumaPrzeciwnika>21:
                wynik = 1
                flagaMoja = True
                flagaPrzeciwnika = True

        if wynik==2:
            if (21-sumaMoja)<(21-sumaPrzeciwnika):
                wynik=1
            elif (21-sumaMoja)>(21-sumaPrzeciwnika):
                wynik=-1
            else:
                wynik=0
        screen.refresh()
        #screen.addstr(12,10,"Wynik: "+wynik)
        if wynik==1:
            rysujWygrana1()
        elif wynik==-1:
            rysujWygrana2()
        else:
            rysujRemis()
        screen.addstr(46,20," ___                 _                                _    _           _  _")
        screen.addstr(47, 20, "|   \ _____ __ _____| |_ _ _  _   _ __ _ _ ____  _ __(_)__| |__  ___  | \| |_____ __ ____ _   __ _ _ _ __ _")
        screen.addstr(48, 20, "| |) / _ \ V  V / _ \ | ' \ || | | '_ \ '_|_ / || / _| (_-< / / |___| | .` / _ \ V  V / _` | / _` | '_/ _` |")
        screen.addstr(49, 20, "|___/\___/\_/\_/\___/_|_||_\_, | | .__/_| /__|\_, \__|_/__/_\_\       |_|\_\___/\_/\_/\__,_| \__, |_| \__,_|")
        screen.addstr(50, 20, "                           |__/  |_|          |__/                                           |___/")
        screen.addstr(51,20, " ____        ____         _")
        screen.addstr(52, 20, "|_  /  ___  |_  /  __ _  | |__  ___   _ _    __   ___")
        screen.addstr(53, 20, " / /  |___|  / /  / _` | | / / / _ \ | ' \  / _| |_ /")
        screen.addstr(54, 20, "/___|       /___| \__,_| |_\_\ \___/ |_||_| \__| /__|")
        screen.refresh()
        screen.addstr(0, 0, "")
        przycisk = screen.getch()  # "Podaj przycisk "
        if przycisk == ord("z"):
            break
        screen.clear()
screen.clear()