#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import io, os, pickle, platform, re, string, sys, json
from colorama import init, Fore, Back, Style
from getkey import getkey, keys
from operator import itemgetter

# core items
items = [
    "Bow (Progressive)",
    "Fire Arrows",
    "Ice Arrows",
    "Light Arrows",
    "Moon Tear",
    "Bomb Bag (Progressive)",
    "Bombchus",
    "Magic Beans",
    "Room Key",
    "Powder Keg",
    "Pictobox",
    "Lens of Truth",
    "Hookshot",
    "Great Fairy's Sword",
    "Letter to Kafei",
    "Land Title Deed",
    "Swamp Title Deed",
    "Mountain Title Deed",
    "Ocean Title Deed",
    "Express Mail to Mama",
    "Pendant of Memories",
    "Bottle",
    "Gold Dust",
    "Chateau Romani",
    "Postman's Hat",
    "All-Night Mask",
    "Blast Mask",
    "Stone Mask",
    "Great Fairy Mask",
    "Deku Mask",
    "Keaton Mask",
    "Bremen Mask",
    "Bunny Hood",
    "Don Gero Mask",
    "Mask of Scents",
    "Goron Mask",
    "Romani Mask",
    "Circus Leader Mask",
    "Kafei Mask",
    "Couple's Mask",
    "Mask of Truth",
    "Zora Mask",
    "Kamaro Mask",
    "Gibdo Mask",
    "Garo Mask",
    "Captain's Hat",
    "Giant's Mask",
    "Fierce Deity Mask",
    "Sword Upgrade",
    "Mirror Shield",
    "Magic (Progressive)",
    "Wallet (Progressive)",
    "Song of Healing",
    "Epona's Song",
    "Song of Storms",
    "Sonata of Awakening",
    "Goron Lullaby",
    "New Wave Bossa Nova",
    "Elegy of Emptiness",
    "Oath to Order"]

# KEY checks
kchecks = [
    "Bow (Progressive)",
    "Fire Arrows",
    "Ice Arrows",
    "Light Arrows",
    "Moon Tear",
    "Bomb Bag (Progressive)",
    "Magic Beans",
    "Room Key",
    "Powder Keg",
    "Pictobox",
    "Lens of Truth",
    "Hookshot",
    "Letter to Kafei",
    "Land Title Deed",
    "Swamp Title Deed",
    "Mountain Title Deed",
    "Ocean Title Deed",
    "Express Mail to Mama",
    "Pendant of Memories",
    "Bottle",
    "Gold Dust",
    "Postman's Hat",
    "All-Night Mask",
    "Blast Mask",
    "Stone Mask",
    "Great Fairy Mask",
    "Deku Mask",
    "Keaton Mask",
    "Bremen Mask",
    "Bunny Hood",
    "Don Gero Mask",
    "Mask of Scents",
    "Goron Mask",
    "Romani Mask",
    "Kafei Mask",
    "Couple's Mask",
    "Mask of Truth",
    "Zora Mask",
    "Kamaro Mask",
    "Gibdo Mask",
    "Garo Mask",
    "Captain's Hat",
    "Giant's Mask",
    "Mirror Shield",
    "Magic (Progressive)",
    "Wallet (Progressive)",
    "Song of Healing",
    "Epona's Song",
    "Song of Storms",
    "Sonata of Awakening",
    "Goron Lullaby",
    "New Wave Bossa Nova",
    "Elegy of Emptiness",
    "Oath to Order"]
kchecks.sort()

# repeatable items
repeatables = [
    "Bow (Progressive)",
    "Bomb Bag (Progressive)",
    "Bombchus",
    "Magic Beans",
    "Bottle",
    "Sword Upgrade",
    "Magic (Progressive)",
    "Wallet (Progressive)"]

# list of checks, full
full_checks = [
    "Vanilla Deku Mask",
    "Vanilla Land Title Deed",
    "CT Scrub trade",
    "Clock Tower HP",
    "Postbox",
    "South CT jumpslash chest",
    "South CT high hookshotable chest",
    "Vanilla Bomber's Notebook",
    "North CT tree",
    "Blast Mask thief",
    "Keaton quiz",
    "Deku Playground",
    "Great Fairy as Human",
    "Great Fairy as Transformed",
    "Tingle at Clock Town",
    "Bank #1",
    "Bank #2",
    "Bank #3",
    "Vanilla Postman's Hat",
    "Postman 10 seconds",
    "Rosa Sisters",
    "Swordsman",
    "Bomb Shop #1",
    "Bomb Shop #2",
    "Vanilla All-Night Mask",
    "Curiosity Shop",
    "Vanilla Chateau Romani Bottle",
    "CT Archery",
    "Honey & Darling",
    "Goron treasure chest minigame",
    "Mayor",
    "Vanilla Circus Leader Mask",
    "Gorman at Bar",
    "Vanilla Kafei Mask",
    "Vanilla Room Key",
    "Vanilla Letter to Kafei",
    "Grandmother #1",
    "Grandmother #2",
    "Toilet",
    #"Vanilla Couple's Mask",
    "Staff Room",
    "Guest Room",
    "Bomber's Hideout chest",
    "East CT high path chest",
    "Vanilla Bremen Mask",
    "Vanilla Pendant of Memories",
    "Vanilla Keaton Mask",
    "Vanilla Express Mail to Mama",
    "Vanilla Moon Tear",
    "Vanilla Kamaro Mask",
    "Gossip Stones",
    "Business Scrub",
    "Peahat grotto",
    "Dodongos grotto",
    "Ikana entrance pillar grotto",
    "Bombchu grotto",
    "Bio Baba",
    "Swamp entrance hidden grotto",
    "Swamp entrance grass chest",
    "Stump chest",
    "Termina Field underwater chest",
    "Tingle at Milk Road",
    "Gorman Race",
    "Vanilla Garo Mask",
    "Cremia",
    "Aliens",
    "Dog Race",
    "Lemons",
    "Vanilla Bunny Hood",
    "Dog Race shed chest",
    "Road to Swamp tree",
    "Road to Swamp grotto"
    "Swamp Archery",
    "Tingle at Woodfall",
    "Swamp Skulltula House",
    "Swamp grotto",
    "Vanilla Magic Beans",
    "Magic Bean grotto high chest",
    "Deku Palace HP",
    "Butler",
    "Vanilla Pictobox",
    "Pictobox Contest",
    "Tingle photograph",
    "Koume's Boat Cruise",
    "Tourist Center hut roof HP",
    "Vanilla Swamp Title Deed",
    "Swamp Scrub trade",
    "Kotake Bottle",
    "Vanilla Red Potion Bottle",
    "Woods grotto",
    "Swamp Great Fairy reward",
    "Great Fairy Spin Attack",
    "Woodfall left chest",
    "Woodfall remote chest",
    "Woodfall HP chest",
    "Smithy #1 (Razor Sword)",
    "Smithy #2 (Gilded Sword)",
    "Vanilla Goron Mask",
    "Darmani",
    "Rock Sirloin",
    "Vanilla Don Gero Mask",
    #"Frog Choir HP",
    "Mountain Village waterfall chest",
    "Tunnel Path grotto",
    "Racetrack grotto",
    "Racetrack bottle",
    "Twin Islands hot spring grotto",
    "Twin Islands underwater chest",
    "Twin Islands hidden path chest",
    "Tingle at Snowhead",
    "Vanilla Mountain Title Deed",
    "Goron Village Scrub trade",
    "Goron Village Scrub Bomb Bag",
    "Goron Village ledge HP",
    "Lens Cave big chest",
    "Vanilla Lens of Truth",
    "Lens Cave bombable chest",
    "Lens Cave invisible chest",
    "Medigoron",
    "Road to Snowhead Scarecrow",
    "Road to Snowhead grotto",
    "Snowhead Great Fairy reward",
    "Great Fairy Extended Magic",
    "Vanilla Zora Mask",
    "Mikau",
    "Lab Fish",
    "Tingle at Great Bay",
    "Ocean Skulltula House HP",
    "Ocean Skulltula House Wallet",
    "Great Bay North Ledge",
    "Fisherman Game",
    "Fisherman Gerudo Picture",
    "Fisherman grotto",
    "Pinnacle Rocke upper chest",
    "Pinnacle Rocke lower chest",
    "Seahorses",
    "Vanilla Ocean Title Deed",
    "Zora Hall Scrub trade",
    "Zora Hall Scrub HP",
    "Zora Hall song >>vAAv>A<<>vv><v",
    "Zora Hall fire arrows",
    "Zora Cape high chest #1",
    "Zora Cape high chest #2",
    "Zora Cape Like Like",
    "Beaver Race",
    "Zora Cape bombable grotto",
    "Zora Cape underwater chest",
    "Great Bay Great Fairy reward",
    "Great Fairy Double Defense",
    "Shiro",
    "Path to Ikana punchable grotto",
    "Path to Ikana high hookshotable chest",
    "Graveyard Bats",
    "Graveyard Iron Knuckle",
    "Graveyard Dampe",
    "Graveyard bombable grotto",
    "Captain Keeta",
    "Vanilla Captain's Hat",
    "Pamela",
    "Vanilla Gibdo Mask",
    "Poe Hut",
    "Ikana Scrub trade",
    "Ikana Scrub far ledge",
    "Secret Shrine grotto",
    "Secret Shrine final prize",
    "Secret Shrine Dinolfos",
    "Secret Shrine Wizzrobe",
    "Secret Shrine Wart",
    "Secret Shrine Garo Master",
    "Ikana Great Fairy reward",
    "Vanilla Great Fairy Sword",
    "Vanilla Mirror Shield",
    "Beneath the Well right path",
    "Beneath the Well left path",
    "Ikana Castle high pillar HP",
    "Stone Tower bean chest #1",
    "Stone Tower bean chest #2",
    "Stone Tower bean chest #3",
    "Woodfall Temple Map chest (Snappers)",
    "Woodfall Temple Compass chest (Dragonflies)",
    "Woodfall Temple Bow chest (Dinolfos)",
    "Odolwa's Remais",
    "Snowhead Temple Map chest (near Bombchu)",
    "Snowhead Temple Compass chest (icy room)",
    "Snowhead Temple FA chest (Wizzrobe)",
    "Goht's Remains",
    "GBT Map chest",
    "GBT Compass chest (near BK)",
    "GBT IA chest (Wart)",
    "Gyorg's Remains",
    "STT Map Chest",
    "STT Compass Chest",
    "STT LA Chest",
    "ISTT Giant's Mask Chest",
    "Twinmold's Remains",
    "PFI low chest",
    "PFI high chest",
    "PFI Hookshot chest (bee hive)",
    "PFI HP chest (3 guards)",
    "PFI egg tank chest",
    "PFE corner chest",
    "PFE near sewers entrance chest",
    "PFE under the log chest",
    "PFS maze chest",
    "PFS spike bombs #1",
    "PFS spike bombs #1",
    "PFS behind gate"]

# woth-valid places
woth_places = [
    #"Beneath Clock Town",
    "South Clock Town",
    "North Clock Town",
    "West Clock Town",
    "East Clock Town",
    "Stock Pot Inn",
    "Laundry Pool",
    "Termina Field",
    "Milk Road",
    "Romani Ranch",
    "Road to Southern Swamp",
    "Southern Swamp",
    "Deku Palace",
    "Woodfall",
    "Woodfall Temple",
    "Mountain Village",
    "Twin Islands",
    "Goron Village",
    "Path to Snowhead",
    "Snowhead",
    "Snowhead Temple",
    "Great Bay Coast",
    "Pinnacle Rock",
    "Zora Hall",
    "Zora Cape",
    "Pirate Fortress Exterior",
    "Pirate Fortress Sewer",
    "Pirate Fortress Interior",
    "Road to Ikana",
    "Ikana Canyon",
    "Ikana Graveyard",
    "Secret Shrine",
    "Beneath the Well",
    "Ikana Castle",
    "Stone Tower",
    "Stone Tower Temple",
    "The Moon"]

def question(type):
    q = {"item": pc("Item?", "c"),
         "location": pc("Check Location?", "r"),
         "whints": pc("Select WOTH location:", "y"),
         "kchecks": pc("Check found there?", "y")}
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

    if qt == "kchecks" and (ct == "woth" or ct == "woth_maybe"):
        r = [e for e in hints if e[0] == "woth" or e[0] == "woth_maybe"]
    else:
        r = [e for e in hints if e[0] == ct]

    if len(r) > 0:
        for h in r:
            if qt == "kchecks":
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

    k = askq(kchecks, "kchecks", "woth")
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
    #print("\n")
    #print(hints)
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
    
main_loop()
