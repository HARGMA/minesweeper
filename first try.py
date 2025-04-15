from numpy import array
from random import randint

m = array([array(["0"] * 10, dtype="U1")] * 10)
m1 = array([array(["_"] * 10, dtype="U1")] * 10)
score = 0
flags = 0
lose = False
lvl = int(input("how many bombs you want(1-99):"))
bombs = 0
while bombs < lvl:
    i = randint(0, 9)
    j = randint(0, 9)
    if m[i, j] == "0":
        m[i, j] = "💣"
        bombs = bombs + 1


def calcul(m, i, j):
    s = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if 0 <= x < 10 and 0 <= y < 10 and (x != i or y != j) and m[x, y] == "💣":
                s = s + 1
    return str(s)


def initial(m):
    for i in range(10):
        for j in range(10):
            if m[i, j] != "💣":
                m[i, j] = calcul(m, i, j)


initial(m)
# print(m)
print(m1)


def saisirCh(ch1, ch2, ch3):
    inp = input(ch3).upper()
    while inp != ch1 and inp != ch2:
        inp = input("entrer :flag/choose:").upper()
    return inp


def saisir(ch):
    n = input(ch)
    while len(n) < 1 or not (n.isdecimal()) or int(n) < 0 or int(n) > 10:
        n = input(ch)
    return int(n)


def flag(m, x, y):
    global flags, score
    if m1[x, y] == "🚩":
        m1[x, y] = "_"
        flags -= 1
        print(m1)
        if m[x, y] == "💣":
            score = score - 1
    elif flags == bombs:
        print("u ran out of flags u should unflag some flags :)")
    else:
        m1[x, y] = "🚩"
        flags += 1
        print(m1)
        if m[x, y] == "💣":
            score = score + 1


def show_bombs(m, m1):
    for i in range(10):
        for j in range(10):
            if m[i, j] == "💣":
                m1[i, j] = "💣"
    print(m1)


def choose(m, m1, x, y):
    global lose
    m1[x, y] = m[x, y]
    if m[x, y] == "💣":
        show_bombs(m, m1)
        print(f"you lost, your score is {score}")
        lose = True
    elif m[x, y] == "0":
        clear(m, m1, x, y)
        print(m1)
    else:
        m1[x, y] = m[x, y]
        print(m1)


def clear(m, m1, x, y):
    tst = True
    while tst:
        tst = False
        for i in range(max(0, x - 1), min(10, x + 2)):  # range(x - 1, x + 2):
            for j in range(max(0, y - 1), min(10, y + 2)):  # range(y - 1, y + 2):
                if 0 <= x < 10 and 0 <= y < 10 and m1[i, j] == "_":
                    m1[i, j] = m[i, j]
                    if m[i, j] == "0":
                        # print(i, j)
                        tst = True
                        # print(m1)
                        clear(m, m1, i, j)


while score < bombs and not (lose):
    y = saisir("donner x:") - 1
    x = saisir("donner y:") - 1
    inp = saisirCh("FLAG", "CHOOSE", "falg/choose:")
    if inp == "FLAG":
        flag(m, x, y)
    elif m1[x, y] == "🚩":
        print("the position is flagged u should unflag it")
    else:
        choose(m, m1, x, y)

    if score == bombs:
        print("congrats u won")
