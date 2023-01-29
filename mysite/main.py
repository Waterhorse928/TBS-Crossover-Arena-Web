from io import TextIOBase
import characters
import os
import random
import sys

DIR_PATH = os.path.dirname(os.path.abspath(__file__))

# -Global Varibles-

turn = 1
round = 0
menu = 1
current = 0
gamemode = 1
partysize = 8
players = 2
wikiList = ["Chen","Cirno","Emilie","Gaius","Keine","Kogasa","Komachi","Marisa","Minoriko","Momiji","Nitori","Olberic","Ophilia","Parsee","Reimu","Rinnosuke","Rumia","Stahl","Sully","Therion","Vaike","Will","Wobuffet","Youmu"]

p1 = {1: characters.Cirno(), 2: characters.Chen(), 3: characters.Chen(), 4: characters.Chen(), 5: characters.Chen(), 6: characters.Chen(), 7: characters.Chen(), 8: characters.Chen()}
p2 = {1: characters.Chen(), 2: characters.Chen(), 3: characters.Chen(), 4: characters.Chen(), 5: characters.Chen(), 6: characters.Chen(), 7: characters.Chen(), 8: characters.Chen()}





# -Functions-

# calls the global player dictonaries. use number to select which player.
def player(number):
    x = "player" + str(number)
    x = globals()[x]
    return x

# sets up global player dictonaries.
def setUpPlayerDict():
    for x in range(0, players):
        player = "player" + str(x)
        globals()[player] = {}



# I need to turn the strings in the player dicts into the classes from characters




# Asks and inputs player slots in order.
def startCharacterSelect():
    for x in range(0, players):
        for y in range(0, partysize):
            print(f"Player {x+1} Slot {y+1}")
            player(x)[y] = wikiCharacterSelect()


# gets key from dict using value
def getKey(d,v):
    for key, value in d.items():
        if v == value:
            return key

#updates current slot numbers on characters (WIP)
def refreshSlot():
    for y in range(0,players):
        for x in range(0, partysize):
            break
            player(y)[x].slot = getKey(player(y),player(y)[x])
            print (x.slot)

#returns a list of character in front
def inFront():
    l = []
    for x in range(0, players):
        for y in range(0, partysize):
            l.append (player(x)[y])
    return l

#sorts list by Spd, Slot, randomly.
def speedOrder(l):
    refreshSlot()
    random.shuffle(l)
    l.sort(key=lambda x : x.slot)
    l.sort(key=lambda x : -x.spd)
    return l



# -MAIN-

def main():
    global menu, round, turn, current, gamemode, partysize, players
    setUpPlayerDict()
    startCharacterSelect()
    battleOver = False
    while battleOver == False:
        refreshSlot()
        print (inFront())
        break




