from vpython import *
from FloorList import *
from Difficulty import *
from restartGame import *

class Player:
	def __init__(self):
		self.bindingPoint = 4
		self.ball = sphere(pos = vector(0, 10, 0), radius = 1, color = color.red)
		self.g = -0.025
		self.v = vector(0, 0, 0)
		self.a = vector(0, self.g, 0)
		self.speed = 0.06
		self.floor = False
	def update(self, floorList, Difficulty, scene):
		self.floorHold(floorList)

		self.a.z -= (self.ball.pos.z-self.bindingPoint)*0.003
		if -0.05 < self.a.z < 0.05:
			self.v.z -= self.v.z/7
		self.v += self.a
		self.ball.pos += self.v
		self.v.x -= self.v.x/7

		self.checkIfDead(Difficulty, floorList, scene)
	def runLeft(self):
		self.a.x = -self.speed
	def runRight(self):
		self.a.x = self.speed
	def runForward(self):
		self.a.z = -self.speed
	def runBackward(self):
		self.a.z = self.speed
	def stopXAxis(self):
		self.a.x = 0
	def stopZAxis(self):
		self.a.z = 0
	def jumpFloor(self):
		if self.v.y - self.g >= 0:
			if  self.floor:
				self.v.y += 0.15
				self.floor = False
			if self.v.y > 0 and not self.floor:
				self.v.y += 0.016
	def checkIfOnFloor(self, floorList):
		for i, Floor in enumerate(floorList):
			box = Floor.box
			if box.pos.y - 0.5 * box.size.y  < self.ball.pos.y - self.ball.radius <= box.pos.y + 0.5 * box.size.y\
			and box.pos.x - 0.5 * box.size.x - 0.3 * self.ball.radius < self.ball.pos.x <\
			box.pos.x + 0.5 * box.size.x + 0.3 * self.ball.radius\
			and box.pos.z - 0.5 * box.size.z - 0.3 * self.ball.radius < self.ball.pos.z <\
			box.pos.z + 0.5 * box.size.z + 0.3 * self.ball.radius:
				box.color = color.yellow
				Floor.a.y = - 0.003
				return i
			else:
				box.color = color.green
				Floor.a.y = 0
		return None
	def floorHold(self, floorList):
		# print(self.v.y)
		boxId = self.checkIfOnFloor(floorList)
		if boxId is not None:
			currentBox = floorList[boxId]
			if self.v.y < -0.025:
				self.v.y *= -0.5
			else:
				if self.floor:
					self.v.y = 0
					self.ball.pos.y = currentBox.box.pos.y + 0.5 * currentBox.box.size.y + self.ball.radius
				self.floor = True
	def checkIfDead(self, Difficulty, FloorList, scene):
		if self.ball.pos.y < -50:
			restartGame(Difficulty, self, FloorList, scene)