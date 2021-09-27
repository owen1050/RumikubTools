import itertools, time, math
from functools import partial
import tkinter as tk

pile = []
decks = []
colors = [0,13,26,39]

straights = []
flushes = []
all_combos = []
solutions = []

indexToCard = ["bl1","bl2","bl3","bl4","bl5","bl6","bl7","bl8","bl9","bl10","bl11","bl12","bl13","bk1","bk2","bk3","bk4","bk5","bk6","bk7","bk8","bk9","bk10","bk11","bk12","bk13","or1","or2","or3","or4","or5","or6","or7","or8","or9","or10","or11","or12","or13","re1","re2","re3","re4","re5","re6","re7","re8","re9","re10","re11","re12","re13"]

def make_pile():
    for c in range(52):
        pile.append(2)
    print("made pile")

def make_straights():
    for c in colors:
        for i in range(13):
            for j in range(13):
                if i + j < 13 and j >= 2 and j < 5:
                    t = []
                    for n in range(j+1):
                        t.append(c+n+i)
                    straights.append(t)
    print("made straights")

def make_flushes():
    for i in range(13):
        t = []
        combos = itertools.combinations(colors, 3)
        for c in combos:
            r = []
            for j in c:
                r.append(i+j)
            flushes.append(r)
        r = []
        for l in colors:
            r.append(l + i)
        flushes.append(r)

def make_all_combos():
    for i in flushes:
        all_combos.append(i)
    for i in straights:
        all_combos.append(i)

def returnNewDeckWithoutHand(hand, deck):
    tempDeck = deck.copy()
    for h in hand:
        if tempDeck[h] > 0:
            tempDeck[h] = tempDeck[h] - 1
        else:
            return False
    return tempDeck
def removeHandFromDeck(hand, deck):
    for h in hand:
        if tempDeck[h] > 0:
            deck[h] = deck[h] - 1
        else:
            return False
    return True

def isHandInDeck(hand, deck):
    tempDeck = deck.copy()
    for h in hand:
        if tempDeck[h] > 0:
            tempDeck[h] = tempDeck[h] - 1
        else:
            return False
    return True

def solveDeck(hands, deck):
    global solutions
    isEmpty = True
    for d in deck:
        if d > 0:
            isEmpty = False
            break
    if isEmpty:
        return hands
    if isSolutionPossible(deck) == False:
        return 0
    for combo in all_combos:
        if isHandInDeck(combo, deck):
            newHands = hands.copy()
            newHands.append(combo)
            ans =  solveDeck(newHands, returnNewDeckWithoutHand(combo, deck))
            if ans != 0:
                return ans
    return 0

def translateDeck(deck):
    if(deck == 0):
        return "No solution"
    ret = []
    for d in deck:
        temp = []
        for c in d:
            temp.append(indexToCard[c])
        ret.append(temp)
    return ret

def action(i):
    global labels, chips, outText
    chipsI = math.floor(i/2)

    if(labels[i].cget('bg') == 'red'):
        labels[i].configure(bg="green")
        chips[chipsI] = chips[chipsI] + 1
    else:
        labels[i].configure(bg="red")
        chips[chipsI] = chips[chipsI] - 1
    print(chips)
    print(isSolutionPossible(chips))

def isSolutionPossible(localChips):
    possAll = True
    for i in range(len(localChips)):
        if localChips[i] != 0:
            possThis = False
            num = i % 13
            checks = []
            if num == 0:
                checks.append([1,2])
            elif num == 1:
                checks.append([-1,1])
                checks.append([1,2])
            elif num == 11:
                 checks.append([-1,1])
                 checks.append([-1,-2])
            elif num == 12:
                checks.append([-1,-2])
            else:
                checks.append([-1,-2])
                checks.append([-1,1])
                checks.append([1,2])

            for check in checks:
                if localChips[check[0]+i] > 0 and localChips[check[1]+i] > 0:
                    possThis = True

            checks = [num, num + 13, num + 26, num + 39]
            count = 0
            for check in checks:
                if(localChips[check] > 0):
                    count = count + 1
            if count > 2:
                possThis = True

            if(possThis == False):
                possAll = False
                break
    return possAll


def updateSolution():
    global labels, chips, outText
    outText.delete('1.0', tk.END)
    isPos = isSolutionPossible(chips)
    if(isPos):
        text = "Solution possible... now thinking"
    else:
        text = "solution impossible"
    outText.insert(tk.INSERT, text)
    time.sleep(0.1)
    if(isPos):
        sol = solveDeck([], chips)
        out = translateDeck(sol)
        outText.delete('1.0', tk.END)
        outText.insert(tk.INSERT, out)

colors_text = ["bl", "bk", "or", "re"]
numbers_text = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

make_pile()
make_straights()
make_flushes()
make_all_combos()

root = tk.Tk()
root.geometry("650x600")
labels = []

incy = 1/(18)
incx = 1/(6)
x = 0
y = 0
j = 0
outText = tk.Text(root)
outText.insert(tk.INSERT,"Select things")
outText.place(relx = incx, rely = incy * 15)
for c in colors_text:
    x = x + 1
    y = 0
    for q in numbers_text:
        y = y + 1

        temp = tk.Button(root, text = c+q, bg="red", command= partial(action,j))
        temp.place(relx = x * incx,
                   rely = y * incy,
                   anchor = 'center')
        labels.append(temp)
        j = j + 1
        temp = tk.Button(root, text =c+q, bg="red",command= partial(action,j))
        temp.place(relx = x * incx + incx*0.5,
                   rely = y * incy,
                   anchor = 'center')
        labels.append(temp)
        j = j + 1

temp = tk.Button(root, text ="Solve", bg="blue",command= partial(updateSolution))
temp.place(relx = 4 * incx + incx*0.5,
           rely = 14 * incy,
           anchor = 'center')

chips = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
root.mainloop()