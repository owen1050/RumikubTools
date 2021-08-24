import itertools
import tkinter as tk
from functools import partial 

pile = []
decks = []
colors = ["r", "b", "k", "o"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
tim = ['r1', 'r2', 'r2', 'r3', 'r4', 'r4', 'r5', 'r5', 'r6', 'r7', 'r7', 'r8', 'r8', 'r9', 'r10', 'r11', 'r12', 'r12', 'r13', 'b1', 'b2', 'b3', 'b4', 'b4', 'b5', 'b5', 'b6', 'b8', 'b8', 'b9', 'b9', 'b10', 'b11', 'b11', 'b12', 'b12', 'b13', 'b13', 'k1', 'k1', 'k2', 'k3', 'k3', 'k4', 'k4', 'k5', 'k5', 'k6', 'k7', 'k9', 'k9', 'k10', 'k10', 'k11', 'k11', 'k12', 'k12', 'k13', 'o1', 'o1', 'o2', 'o2', 'o3', 'o3', 'o4', 'o4', 'o5', 'o5', 'o6', 'o7', 'o7', 'o8', 'o8', 'o10', 'o10', 'o11', 'o12', 'o13']
solutions = []

straights = []
flushes = []
all_combos = []

def make_pile():
    for c in colors:
        for n in numbers:
            pile.append(c+n)
            pile.append(c+n)
    print("made pile")

def make_straights():
    for c in colors:
        for i in range(13):
            for j in range(13):
                if i + j < 13 and j >= 2:
                    t = []
                    for n in numbers[i:i+j+1]:
                        t.append(c+n)
                    straights.append(t)
    print("made straights")

def make_flushes():
    

    for i in range(13):
        t = []
        combos = itertools.combinations(colors, 3)
        for c in combos:
            r = []
            for j in c:
                r.append(j+str(i+1))
            flushes.append(r)
        r = []
        for l in colors:
            r.append(l+str(i+1))
        flushes.append(r)

def make_all_combos():
    for i in flushes:
        all_combos.append(i)
    for i in straights:
        all_combos.append(i)

def solve(tiles, runs):
    #print(len(tiles))
    if len(tiles) == 0:
        solutions.append(runs)
    for combo in all_combos:
        to_rem = []
        for tile in combo:
            if tile in tiles:
                to_rem.append(tile)
            else:
                break
        if to_rem == combo:
            newRuns = runs.copy()
            newRuns.append(to_rem)
            newTiles = remove_tiles(tiles.copy(), to_rem)
            solve(newTiles, newRuns)

def remove_tiles(t1, to_rem):
    for r in to_rem:
        t1.remove(r)
    return t1


make_pile()
make_straights()
make_flushes()
make_all_combos()

root = tk.Tk()
root.geometry("600x600")
labels = []

incy = 1/(13+2)
incx = 1/(4+2)
x = 0
y = 0

def make_deck():
    global decks
    td = []
    i = 0;
    for l in labels:
        if(l.cget('bg') == 'green'):
            td.append(pile[i])
        i = i + 1
    if len(td) == 0 and len(decks) > 0:
        pass
    else:
        decks = td.copy()

def action(i):
    if(labels[i].cget('bg') == 'white'):
        labels[i].configure(background="green")
    else:
        labels[i].configure(background="white")
    make_deck()

for c in colors:
    x = x + 1
    y = 0
    for i in numbers:
        y = y + 1
        temp = tk.Button(root, text =pile[len(labels)], background="white", command= partial(action,len(labels)))
        temp.place(relx = x * incx,
                   rely = y * incy,
                   anchor = 'center')
        labels.append(temp)
        temp = tk.Button(root, text =pile[len(labels)], background="white",command= partial(action,len(labels)))
        temp.place(relx = x * incx + incx*0.5,
                   rely = y * incy,
                   anchor = 'center')
        labels.append(temp)

root.mainloop()
decks = tim.copy()
print(decks)
solve(decks, [])
