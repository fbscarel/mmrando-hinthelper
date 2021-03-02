#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io, os, pickle, platform, re, string, sys, yaml
from colorama import init, Fore, Back, Style
from getkey import getkey, keys
from operator import itemgetter

def question(type):
    q = {"item": pc("Item?", "c"),
         "location": pc("Check Location?", "r"),
         "whints": pc("Select WOTH location:", "y"),
         "kitems": pc("Item found there?", "y")}
    return q.get(type)

def pc(text, color):
    op = {"b": Fore.BLACK,
          "r": Fore.RED,
          "g": Fore.GREEN,
          "y": Fore.YELLOW,
          "u": Fore.BLUE,
          "m": Fore.MAGENTA,
          "c": Fore.CYAN,
          "w": Fore.WHITE}
    return op.get(color) + text + Style.RESET_ALL

def bc(text, color):
    return Back.CYAN + text + Style.RESET_ALL

def pexit():
    sys.exit()

def askq(olist, qt, ct):
    global hints
    plist = olist[:]
    s = ""
    i = 0

    if qt == "kitems" and (ct == "woth" or ct == "woth_maybe"):
        r = [e for e in hints if e[0] == "woth" or e[0] == "woth_maybe"]
    else:
        r = [e for e in hints if e[0] == ct]

    if len(r) > 0:
        for h in r:
            if qt == "kitems":
                for item in h[2:]:
                    if item in plist and item not in repeatables:
                        plist.remove(item)
            else:
                if h[1] in plist and h[1] not in repeatables:
                    plist.remove(h[1])

    while True:
        os.system(clearstr)

        r = re.compile(".*" + s + ".*", re.IGNORECASE)
        nlist = list(filter(r.match, plist))

        print(question(qt) + "\n")

        if len(s) >= 0:
            for x, y in enumerate(nlist):
                if x == i:
                    print(bc(y, "y"))
                else:
                    print(y)

        print("\n====================================================================")

        if len(s) > 0:
            print(pc("\n[UP and DOWN to scroll through list, ENTER to select, ESC to cancel]", "c"), end="")
            #print(pc("\n['<' and '>' to scroll through list, ENTER to select, ESC to cancel]", "c"), end="")
            print(pc("\nFilter: ", "u") + s, end="")
        else:
            print(pc("\nFilter: ", "u") + "[Type at least one letter to search, ESC to cancel]", end="")

        c = getkey()
        if c == keys.BACKSPACE or c == keys.DELETE:
            s = s[:-1]
        elif (c == keys.UP or c == keys.LEFT) and i > 0:
        #elif (c == keys.ANGLE or c == keys.TAIL) and i > 0:
            i -= 1
        elif (c == keys.DOWN or c == keys.RIGHT) and i < len(nlist) - 1:
        #elif (c == keys.RIGHT_ANGLE or c == keys.SPOT) and i < len(nlist) - 1:
            i += 1
        elif c == keys.ENTER:
            return nlist[i]
        elif c == keys.ESC:
            raise Exception('Break out')
        elif c.isalnum():
            s = s + c
            i = 0
        else:
            pass

def ghint(ct):
    global hints

    if ct == "item":
        s = askq(items, "item", ct)

    if ct == "woth" or ct == "fool":
        c = askq(woth_places, "location", ct)
    else:
        c = askq(full_checks, "location", ct)

    if ct == "item":
        hints.append([ct, s, c])
    elif ct == "woth":
        set = False
        for index, hint in enumerate(hints):
            if hint[1] == c:
                hints[index][0] = "woth"
                set = True
        if not set:
            hints.append([ct, c])
    else:
        hints.append([ct, c])

    main_loop()

def item_hint():
    ghint("item")

def dead_hint():
    ghint("dead")

def woth_edit():
    global hints

    k = askq(kitems, "kitems", "woth")
    s = askq(woth_places, "location", "woth_edit")

    set = False
    for index, hint in enumerate(hints):
        if hint[1] == s:
            hints[index].append(k)
            set = True

    if not set:
        hints.append(["woth_maybe", s, k])

    main_loop()

def woth_hint():
    ghint("woth")

def fool_hint():
    ghint("fool")

def phint(type, text, check):
    global hints

    r = [e for e in hints if e[0] == type]

    if len(r) > 0:
        print("\n" + text)

        r = sorted(r, key=itemgetter(1))
        for h in r:
            if check == "long":
                print("\t" + h[1] + pc(" is at ","m") + h[2])
            elif check == "woth":
                print("\t" + h[1] + " (" + ', '.join(h[2:]) + ")")
            else:
                print("\t" + h[1])

def undo_hint():
    global hints

    print(hints[-1])
    del hints[-1]
    main_loop()

def kill_hint():
    global hints

    hints.clear()
    main_loop()

def loadf():
    global fname, hints
    if os.path.isfile(fname) and os.stat(fname).st_size != 0:
        f = open(fname, "rb")
        hints = pickle.load(f)
        f.close()

def writef():
    global fname, hints
    f = open(fname, "wb")
    pickle.dump(hints, f)

def main_hints():
    phint("woth", pc("Way of the Hero:", "y"), "woth")
    phint("fool", pc("Barren Locations:", "r"), "short")
    phint("item", pc("Items:", "c"), "long")
    phint("dead", pc("Dead Checks:", "u"), "short")

def main_prompt():
    #global hints
    op = {"i": item_hint,
          "d": dead_hint,
          "w": woth_hint,
          "f": fool_hint,
          "u": undo_hint,
          "k": kill_hint,
          "n": woth_edit,
          "e": pexit}

    print("\n=====================================================================")
    print("\n" + pc("(W)","y") + "oth | " + pc("(N)","g") + "ew Check | " + pc("(F)","r") + "ool | " + pc("(I)","c") + "tem | " + pc("(D)","u") + "ead")
    print("\n" + pc("(U)","w") + "ndo | " + pc("(K)","w") + "ill | " + pc("(E)","w") + "xit ", end="")
    c = getkey()
    try:
        op[c.lower()]()
    except SystemExit:
        print()
        writef()
        pass
    except:
        main_loop()

def main_loop():
    os.system(clearstr)
    main_hints()
    main_prompt()

hints = []
if platform.system() == "Windows":
    fname = ".\\.hinthelper.p"
    clearstr = "cls"

else:
    fname = "./.hinthelper.p"
    clearstr = "clear"

init()
loadf()

items = []
kitems = []
repeatables = []
with open('items.yaml', 'r') as f:
    i = yaml.full_load(f)
    for k in i['items']:
        items.append(k['name'])
        if k['opens_checks'] == True:
            kitems.append(k['name'])
        if k['is_repeatable'] == True:
            repeatables.append(k['name'])

woth_places = []
full_checks = []
with open('locations.yaml', 'r') as f:
    i = yaml.full_load(f)
    for k in i['locations']:
        woth_places.append(k['name'])
        for c in k['checks']:
            full_checks.append(c)

main_loop()
