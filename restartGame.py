from vpython import *

def restartGame(Difficulty, P, L, scene):
	Difficulty.resetParam()

	P.ball.pos = vector(0, 10, 0)
	P.v = vector(0, 0, 0)
	P.a = vector(0, P.g, 0)
	P.floor = False
	for floor in L:
		floor.box.visible = False
	L.clear()

	for i in range(7):
		L.addtoEnd(Difficulty)
	scene.waitfor('keydown')