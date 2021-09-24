import itertools, time
from functools import partial 

pile = []
decks = []
colors = [0,13,26,39]

straights = []
flushes = []
all_combos = []
solutions = []

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
    for combo in all_combos:
        if isHandInDeck(combo, deck):
            newHands = hands.copy()
            newHands.append(combo)
            ans =  solveDeck(newHands, returnNewDeckWithoutHand(combo, deck))
            if ans != 0:
                return ans
    return 0

make_pile()
make_straights()
make_flushes()
make_all_combos()

i = [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 2, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 2, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 2, 1, 1, 1]

print(solveDeck([], i))