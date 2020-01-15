from vpython import *
from random import uniform

from Player import *
from Keyboard import *
from FloorList import *
from Difficulty import *
from restartGame import *


class Floor:
	def __init__(self, pos, size, v):
		self.box = box(pos = pos, size = size, color = color.green)
		self.v = v
		self.a = vector(0, 0, 0)
		self.bindingPoint = self.box.pos.y
	def update(self, Difficulty):

		# print(self.a.y, self.box.pos.y - self.bindingPoint)
		self.a.y -= (self.box.pos.y-self.bindingPoint)*0.003
		self.a.y = round(self.a.y, 3)
		if -0.01 < self.a.y < 0.01:
			self.v.y -= self.v.y*0.1
			# self.a.y = 0
		self.v += self.a
		self.box.pos += self.v
		# self.v.x -= self.v.x/7

		self.v.z = Difficulty.SPEED