import pygame
from pygame.locals import *
import sys

def main():
	wight, height = 400, 400
	x, y = wight/2, height/2

	#初期化
	pygame.init()

	#画面設定
	pygame.display.set_mode((wight,height),0,32)
	screen = pygame.display.get_surface()
	font = pygame.font.Font(None,15)

	while(1):

		
		if x<0:
			x = 0
		if x>wight:
			x = wight
		if y<0:
			y = 0
		if y>height:
			y = height

		pressKey = pygame.key.get_pressed()
		if pressKey[K_LEFT]:
			x -= 3
		if pressKey[K_RIGHT]:
			x += 3
		if pressKey[K_UP]:
			y -= 3
		if pressKey[K_DOWN]:
			y += 3

		screen.fill((225,225,225)) 
		text = font.render("runner",True,(0,0,0))
		screen.blit(text,[x-10,y-13])
		pygame.draw.rect(screen,(225,0,0),Rect(x,y,10,10))
		pygame.display.update()

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()


if __name__ == "__main__":
	main()
