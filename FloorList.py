from vpython import *
from random import uniform

from Player import *
from Floor import *
from Keyboard import *
from Difficulty import *
from restartGame import *

class FloorList(list):

	def addtoEnd(self, D):
		if len(self) == 0:
			distance = 0
			myLength = 40
			position = 0
		else:
			lastBox = self[-1].box
			myLength = uniform(20,D.LEN) #50
			distance = lastBox.pos.z - lastBox.size.z*0.5 - myLength*0.5 - uniform(2 - D.DIST, D.DIST) 
			position = -40
			while position < -15 or position > 15:
				position = uniform(lastBox.pos.x - 10,lastBox.pos.x + 10)

		self.append(Floor(
				pos = vector(position, 0 , distance),
				size = vector(D.WIDTH, 1, myLength), #4
				v=vector(0, 0, D.SPEED))) #0.3
		# print(D.LEN, D.WIDTH, D.SPEED, D.DIST)

	def checkIfdelete(self, Difficulty):
		for i, floor in enumerate(self):
			if floor.box.pos.z - floor.box.size.z > 15:
				floor.box.visible = False
				self.addtoEnd(Difficulty)
				self.pop(i)