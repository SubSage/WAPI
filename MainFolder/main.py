import pygame
import sys
from Vector2 import Vector2
from Circles import Circles
from GenerateMap import GameMap

def LoadingScreen(state):
        if state == 0:
                return "Initializing game map..."
        elif state == 1:
                return "Finding locations..."
        elif state == 2:
                return "Finding people..."
        elif state == 3:
                return "Rendering..."

ZONE_RADIUS = 100
pygame.init()
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), pygame.FULLSCREEN)
screen_w, screen_h = screen.get_size()
pygame.display.set_caption("WAPI")

font = pygame.font.Font(None, 20)
text = font.render(LoadingScreen(0), 1, (255, 255, 255))
screen.blit(text, (screen_w/2, screen_h/2))
pygame.display.flip()


screen.fill((0,0,0))


gameMap = GameMap("Vlad the Impaler", 20, 5, Vector2(100 + screen_w, 100 + screen_h))
gameMap.chooseCities(gameMap.villain)

screen.fill((0,0,0))
text = font.render(LoadingScreen(1), 1, (255, 255, 255))
screen.blit(text, (screen_w/2, screen_h/2))
pygame.display.flip()

gameMap.addLocationsToMap(ZONE_RADIUS)

for l in gameMap.mapOfLocations.map.values():
        print l

screen.fill((0,0,0))
text = font.render(LoadingScreen(2), 1, (255, 255, 255))
screen.blit(text, (screen_w/2, screen_h/2))
pygame.display.flip()

gameMap.choosePeople(gameMap.villain)
gameMap.makeListOfPeople()

for p in gameMap.listOfPeople:
        print p

screen.fill((0,0,0))
text = font.render(LoadingScreen(3), 1, (255, 255, 255))
screen.blit(text, (screen_w/2, screen_h/2))
pygame.display.flip()


listOfCircles = []
listOfPlaces = []
listOfCoordinates = []
for k in gameMap.mapOfLocations.map.keys():
        listOfCircles += [Circles(60, k)]

while(True):
        pygame.event.pump()
        for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

        screen.fill((0,0,0))
        for c in listOfCircles:
                c.draw(screen)

        for k in gameMap.mapOfLocations.map.keys():
                text = font.render(gameMap.mapOfLocations.map[k], 1, (255, 255, 255))
                screen.blit(text, (k.x - text.get_width()/2, k.y - text.get_height()/2))
        pygame.display.flip()



