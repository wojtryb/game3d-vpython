from vpython import *
from random import uniform

from Player import *
from Floor import *
from FloorList import *
from Difficulty import *
from restartGame import *


class Keyboard:
	def __init__(self):
		pass
	def checkKeyboard(self, Player, Difficulty, FloorList, scene):
		k = keysdown() # a list of keys that are down
		if 'a' in k: Player.jumpFloor()
		if 'left' in k: Player.runLeft()
		if 'right' in k: Player.runRight()
		if 'up' in k: Player.runForward()
		if 'down' in k: Player.runBackward()
		if 'right' not in k and 'left' not in k: Player.stopXAxis()
		if 'up' not in k and 'down' not in k: Player.stopZAxis()
		if 'r' in k: restartGame(Difficulty, Player, FloorList, scene)