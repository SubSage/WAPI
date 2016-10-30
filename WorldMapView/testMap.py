import pygame
import sys
from Circles import Circles

pygame.init()

infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)
screen_w, screen_h = screen.get_size()
pygame.display.set_caption("hi there")

font = pygame.font.Font(None, 20)
text = font.render("Hello World!", 1, (255, 255, 255))

screen.fill((0,0,0))

circ = Circles(80, (screen_w/2 + text.get_width()/2, screen_h/2))

while True:
	pygame.event.pump()
	for evt in pygame.event.get():
		if evt.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE:
			pygame.quit()
			sys.exit()


	circ.draw(screen)
	screen.blit(text, (screen_w/2, screen_h/2))
	pygame.display.flip()