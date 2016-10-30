import pygame

class Circles:
	def __init__(self, r, c):
		self.radius = r
		self.coords = c

	def draw(self, surf):
		pygame.draw.circle(surf, (0,0,0), (self.coords.x, self.coords.y), self.radius, 0)
		pygame.draw.circle(surf, (255,255,255), (self.coords.x, self.coords.y), self.radius, 2)
	