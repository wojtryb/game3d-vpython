from vpython import *

class Difficulty:
	def __init__(self):
		self.resetParam()
	def resetParam(self):
		self.DIST = 0
		self.LEN = 50
		self.WIDTH = 7
		self.SPEED = 0.3
	def updateDifficulty(self):
		if self.DIST < 50:
			self.DIST += 0.03
		if self.LEN > 20:
			self.LEN -= 0.01
		if self.WIDTH >3.5:
			self.WIDTH -= 0.004
		if self.SPEED < 0.7:
			self.SPEED += 0.0002