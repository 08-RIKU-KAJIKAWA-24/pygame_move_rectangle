import pygame
from pygame.locals import *
import random
import sys

SCR = Rect(0,0,600,600)
CS = 10
ROW = int(SCR.height / CS)
COL = int(SCR.width / CS)

DEAD = 0
ALIVE = 1

FLAG = 0.15

class LifeGame:

	def __init__(self):
		pygame.init()
		screen = pygame.display.set_mode(SCR.size)
		pygame.display.set_caption("Life Game")
		self.font = pygame.font.SysFont(None,20)
		self.field = [[DEAD for i in range(ROW)] for j in range(COL)]
		#世代
		self.generation = 0
		#実行可能状態か否かの判定(Falseは実行可能不可/trueは実行可能)
		self.run = False
		self.cursor = [ROW/2, COL/2]
		self.clear()
		while True:
			self.drawField(screen)
			self.simulate()
			pygame.display.update()
			pressKey = pygame.key.get_pressed()
			if pressKey[K_LEFT]:
				self.cursor[0] -= 1
				if self.cursor[0] <= 0: self.cursor[0] = 0
			if pressKey[K_RIGHT]:
				self.cursor[0] += 1
				if self.cursor[0] >= COL: self.cursor[0] = COL
			if pressKey[K_UP]:
				self.cursor[1] -= 1
				if self.cursor[1] <= 0: self.cursor[1] = 0
			if pressKey[K_DOWN]:
				self.cursor[1] += 1
				if self.cursor[1] >= ROW: self.cursor[1] = ROW
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						pygame.quit()
						sys.exit()
					elif event.key == K_LEFT:
						self.cursor[0] -= 1
						if self.cursor[0] <= 0: self.cursor[0] = 0
					elif event.key == K_RIGHT:
						self.cursor[0] += 1
						if self.cursor[0] >= COL: self.cursor[0] = COL
					elif event.key == K_DOWN:
						self.cursor[1] += 1
						if self.cursor[1] >= ROW: self.cursor[1] = ROW
					elif event.key == K_UP:
						self.cursor[1] -= 1
						if self.cursor[1] <= 0: self.cursor[1] = 0

					elif event.key == K_SPACE:
						x = int(self.cursor[1])
						y = int(self.cursor[0])
						if self.field[y][x] == DEAD:
							self.field[y][x] = ALIVE
						elif self.field[y][x] == ALIVE:
							self.field[y][x] = DEAD

					elif event.key == K_c:
						self.clear()

					elif event.key == K_n:
						self.step()

					elif event.key == K_s:
						self.run = not self.run

					elif event.key == K_r:
						self.randomAddAlive()


	#シムレーションの初期化
	def clear(self):
		self.generation = 0
		for j in range(ROW):
			for i in range(COL):
				self.field[j][i] = DEAD

	def drawField(self, screen):
		for j in range(ROW):
			for i in range(COL):
				if self.field[j][i] == DEAD:
					pygame.draw.rect(screen, (0,0,0), Rect(j*CS,i*CS,CS,CS))
				else:
					pygame.draw.rect(screen ,(0,225,0),Rect(j*CS,i*CS,CS,CS))

				#glid
				pygame.draw.rect(screen, (50,50,50), Rect(j*CS,i*CS,CS,CS),1)

		#cursor
		pygame.draw.rect(screen, (225,225,0), Rect(CS*self.cursor[0],CS*self.cursor[1],CS,CS),2)
		screen.blit(self.font.render("GENERATION:%d" % self.generation, True, (225,225,0)), (0,0))
		screen.blit(self.font.render("space : BIRTH/KILL", True, (225,225,0)), (0,12))
		screen.blit(self.font.render("s : start/stop", True, (225,225,0)), (0,24))
		screen.blit(self.font.render("n : next", True, (225,225,0)), (0,36))
		screen.blit(self.font.render("r : random", True, (225,225,0)), (0,48))

	def simulate(self):
		if self.run: 
			self.step()

	def randomAddAlive(self):
		for i in range(ROW):
			for j in range(COL):
				if random.random() < FLAG:
					self.field[j][i] = ALIVE

	def countAliveCells(self, x, y):
		cnt = 0
		if x == 0 or x == COL-1 or y == 0 or y == ROW-1:
			return cnt
		cnt += self.field[y-1][x-1]
		cnt += self.field[y-1][x]
		cnt += self.field[y-1][x+1]
		cnt += self.field[y][x-1]
		cnt += self.field[y][x+1]
		cnt += self.field[y+1][x-1]
		cnt += self.field[y+1][x]
		cnt += self.field[y+1][x+1]
		return cnt

	def step(self):
		nextField = [[False for i in range(COL)] for j in range(ROW)]
		for i in range(ROW):
			for j in range(COL):
				alive_cells_num = self.countAliveCells(i,j)
				if alive_cells_num == 2:
					nextField[j][i] = self.field[j][i]
				elif alive_cells_num == 3:
					nextField[j][i] = ALIVE
				else:
					nextField[j][i] = DEAD
		self.field = nextField
		self.generation += 1


if __name__ == "__main__":
	LifeGame()
