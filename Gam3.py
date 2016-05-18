# We usually play a game called werewolf in AP Psychology since the AP exams are over
# and we got nothing to do. Our teacher uses paper to distribute the roles of each
# person, NW being Not Werewolf and W being Werewolf. When it is time to recollect
# the papers, a particular student thinks it is best to wrap the paper and essentially
# ruin the game by making it obvious that his paper is either W or NW next game.
# This code was written with the anger fueled by him, so thank him for the inspiration.
# P.S. this is my first python file and code, so feel free to help me out. Thank you!

import random

# Strings. werewolves and not werewolves.
w = "a werewolf."
nw = "not a werewolf."
clear = "\n" * 100

# gotta make sure they know how many people are playing.
print "This game is for 10 people only."

# I will try to make this as simple as possible.
# P1 will represent the first player. the teacher or narrator will
# have this application, and instead give out a label with each player
# number. The player number will get the string of either W or NW.

# Array and Rands.
items = [w, nw]
rand_r1 = random.choice(items)
rand_r2 = random.choice(items)
rand_r3 = random.choice(items)
rand_r4 = random.choice(items)
rand_r5 = random.choice(items)
rand_r6 = random.choice(items)
rand_r7 = random.choice(items)
rand_r8 = random.choice(items)
rand_r9 = random.choice(items)
rand_r10 = random.choice(items)

# The players, getting assigned random strings.

p1 = rand_r1
p2 = rand_r2
p3 = rand_r3
p4 = rand_r4
p5 = rand_r5
p6 = rand_r6
p7 = rand_r7
p8 = rand_r8
p9 = rand_r9
p10 = rand_r10

# I need a way to make sure that there are at most 1, 2, or 3 werewolves.


# Time to print!
print "Player 1 is ", p1
try:
    input("Let the first player know before you press enter.")
except SyntaxError:
    pass
print clear
print "Player 2 is ", p2
try:
    input("Let the second player know before you press enter.")
except SyntaxError:
    pass
print clear
print "Player 3 is ", p3
try:
    input("Let the third player know before you press enter.")
except SyntaxError:
    pass
print clear
print "Player 4 is ", p4
try:
    input("Let the fourth player know before you press enter.")
except SyntaxError:
    pass
print clear
print "Player 5 is ", p5
try:
    input("Let the fifth player know before you press enter.")
except SyntaxError:
    pass
print clear
print "Player 6 is ", p6
try:
    input("Let the sixth player know before you press enter.")
except SyntaxError:
    pass
print clear
print "Player 7 is ", p7
try:
    input("Let the seventh player know before you press enter.")
except SyntaxError:
    pass
print clear
print "Player 8 is ", p8
try:
    input("Let the eighth player know before you press enter.")
except SyntaxError:
    pass
print clear
print "Player 9 is ", p9
try:
    input("Let the ninth player know before you press enter.")
except SyntaxError:
    pass
print clear
print "Player 10 is ", p10
try:
    input("Let the tenth player know before you press enter.")
except SyntaxError:
    pass
print clear

# This is for the teacher or narrator to use.
try:
    input("The following will be the roles of each player.")
except SyntaxError:
    pass
print "Player 1 is ", p1
print "Player 2 is ", p2
print "Player 3 is ", p3
print "Player 4 is ", p4
print "Player 5 is ", p5
print "Player 6 is ", p6
print "Player 7 is ", p7
print "Player 8 is ", p8
print "Player 9 is ", p9
print "Player 10 is ", p10

# print clear is just a hundred lines of nothing because I gave up on trying to clear
# the GUI or whatever I will be using. What does need to be fixed is that there should
# be only 1 or 2 werewolves, that is all. I hope this isn't terrible for a beginner.

