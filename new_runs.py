import itertools, time
from functools import partial 

pile = []
decks = []
colors = ["b", "k", "o", "r"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]

straights = []
flushes = []
all_combos = []

bthT = 0
hashes = {}

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
                if i + j < 13 and j >= 2 and j < 5:
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

def remove_tiles(t1, to_rem):
    for r in to_rem:
        t1.remove(r)
    return t1

make_pile()
make_straights()
make_flushes()
make_all_combos()

def generate_possible_board(tiles, runs):
    global bthT
    run_hash = board_to_hash(runs)
    if(run_hash in hashes):
        return 0
    hashes[run_hash] = runs
    if(len(tiles) < 3):
        return 0
    for combo in all_combos:
        match = 0
        l = len(combo)
        for tile in combo:
            if tile in tiles:
                match = match + 1
            else:
                break
        if match == l:
            bthi0 = time.time()
            newRuns = runs.copy()
            newRuns.append(combo)
            newTiles = remove_tiles(tiles.copy(), combo)
            bthT = bthT + (time.time() - bthi0)
            generate_possible_board(newTiles, newRuns)

def board_to_hash(board):
    global bthT

    chips = []
    for run in board:
        for chip in run:
            chips.append(chip)
    ret = ""
    for chip in sorted(chips):
        ret = ret + chip

    return ret


t0 = time.time()
generate_possible_board(pile[0:3*int(len(pile)/7)], [])
print(len(hashes))
t1 = time.time()
print(t1-t0, bthT)
while(True):
    time.sleep(1)


#check % of time certain functions are running and then nuke them or time them
#remove tiles takes 10% and board to hash takes 25%