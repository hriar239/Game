# We usually play a game called werewolf in AP Psychology since the AP exams are over
# and we do not have anything to do. Our teacher uses paper to distribute the roles of each
# person, NW being Not Werewolf and W being Werewolf. When it is time to recollect
# the papers, a particular student thinks it is best to wrap the paper and essentially
# ruin the game by making it obvious that his paper is either W or NW next game.
# This code was written with the anger fueled by him, so thank him for the inspiration.
# P.S. this is my first python file and code, so feel free to help me out. Thank you!

# REVISION 2

import random
import itertools

# Strings. Not sure if I will use all of them.
nw = "not a werewolf."
w = "a werewolf."
b = "a bodyguard."
nm = "a witch."
plr = "Player"
i = "is"

# List for minimum of 8 people.
items = [nw, nw, nw, nw, w, w, b, nm]

# Random shuffle. This is useful because instead of randomizing and selecting, it
# shuffles the list itself.
rand1 = random.shuffle(items)


# In this case, I'll attempt to let you choose as many players as you want.
print('Hello! How many players?')
n = input()

# A while loop to make sure you do not choose less than 8 players.
while n < 7:
    input("Sorry, you have to enter anything above 8: ")
    n = 8

g = 0  # The first player will be called "Player 0"
t = n - 8  # equation for more nws

# This if statement includes a for loop that adds more nws.
if n >= 8:
    for nw in itertools.repeat(nw, t):
        items = [nw] + items

# This is the last part. it will print out all the stuff. I had preferred something
# like individually showing each player, but the narrator can just collect the papers
# or sticky notes from the players.

for items in itertools.repeat(items, n):
    print plr, g, i, items[g]
    g += 1

# Thanks to my brother for telling me to use for/while loops instead of rands and
# variables only.
