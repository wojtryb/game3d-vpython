from vpython import *
from random import uniform

from Player import *
from Floor import *
from Keyboard import *
from FloorList import *
from Difficulty import *
from restartGame import *

#-----------------------Main

D = Difficulty()

scene = canvas(title="my game", width = 800, height = 600,
	center=vector(0,12,20), userzoom = False, userspin = False, autoscale = False)
P = Player()
K = Keyboard()
L = FloorList()

restartGame(D, P, L, scene)

dt = 0.01
t = 0
dv = 0.2

while(True):
	rate(60)
	K.checkKeyboard(P, D, L, scene)
	P.update(L, D, scene)
	L.checkIfdelete(D)
	for F in L:
		F.update(D)
	D.updateDifficulty()
	t+=dt