import itertools, time
from functools import partial 

pile = []
decks = []
colors = ["b", "k", "o", "r"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
tim = ['r1', 'r2', 'r2', 'r3', 'r4', 'r4', 'r5', 'r5', 'r6', 'r7', 'r7', 'r8', 'r8', 'r9', 'r10', 'r11', 'r12', 'r12', 'r13', 'b1', 'b2', 'b3', 'b4', 'b4', 'b5', 'b5', 'b6', 'b8', 'b8', 'b9', 'b9', 'b10', 'b11', 'b11', 'b12', 'b12', 'b13', 'b13', 'k1', 'k1', 'k2', 'k3', 'k3', 'k4', 'k4', 'k5', 'k5', 'k6', 'k7', 'k9', 'k9', 'k10', 'k10', 'k11', 'k11', 'k12', 'k12', 'k13', 'o1', 'o1', 'o2', 'o2', 'o3', 'o3', 'o4', 'o4', 'o5', 'o5', 'o6', 'o7', 'o7', 'o8', 'o8', 'o10', 'o10', 'o11', 'o12', 'o13']
basic = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6']
solutions = []

straights = []
flushes = []
all_combos = []

solved_board = []
solution_hashes = {}
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

def solve(tiles, runs):
    if len(tiles) == 0:
        solutions.append(runs)
        print(runs)
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

def generate_possible_board(tiles, runs):
    if(board_to_hash(runs) in hashes):
        return 0
    if(len(runs) == 2):
        print(runs)
    solved_board.append(runs)
    if(len(solved_board) % 1000000 == 0):
        print(len(solved_board))
    if(len(tiles) < 3):
        return 0
    for combo in all_combos:
        match = 0
        for tile in combo:
            if tile in tiles:
                match = match + 1
            else:
                break
        if match == len(combo):
            newRuns = runs.copy()
            newRuns.append(combo)
            newTiles = remove_tiles(tiles.copy(), combo)
            generate_possible_board(newTiles, newRuns)

def board_to_hash(board):
    chips = []
    for run in board:
        for chip in run:
            chips.append(chip)
    ret = ""
    for chip in sorted(chips):
        ret = ret + chip
    return ret

def hash_boards(solved_board):

    for board in solved_board:
        hash = board_to_hash(board)
        hashes[hash] = board
    return hashes

def generate_all_hash(boards):
    hashes = {}
    for board in boards:
        pass



t0 = time.time()
generate_possible_board(pile[0:int(len(pile)/5)], [])
print(len(solved_board))
hashed_board = hash_boards(solved_board)
print(len(hashed_board))
t1 = time.time()
print(t1-t0)

#check hash before we continue because we can kill entire trunks