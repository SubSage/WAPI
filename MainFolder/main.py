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
FURTHEST_UP = 0
FURTHEST_DOWN = 0
FURTHEST_LEFT = 0
FURTHEST_RIGHT = 0
X_OFFSET = 0
Y_OFFSET = 0

camera = Vector2(0, 0)

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


gameMap = GameMap("Voldemort", 10, 5, Vector2(100 + screen_w, 100 + screen_h))
gameMap.chooseCities(gameMap.villain)

screen.fill((0,0,0))
text = font.render(LoadingScreen(1), 1, (255, 255, 255))
screen.blit(text, (screen_w/2, screen_h/2))
pygame.display.flip()

gameMap.addLocationsToMap(ZONE_RADIUS)

listOfPlaces = []

for l in gameMap.mapOfLocations.map.values():
        listOfPlaces += [l]
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
for k in gameMap.mapOfLocations.map.keys():
        listOfCircles += [Circles(60, k)]


index = 0;
while(True):
        screen.fill((0,0,0))
        pygame.event.pump()
        for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                elif evt.type == pygame.KEYDOWN and evt.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

        camera.x = pygame.mouse.get_pos()[0]
        camera.y = pygame.mouse.get_pos()[1]
        for c in listOfCircles:
                c.draw(screen, camera)


        
        for k in gameMap.mapOfLocations.map.keys():
                if index < len(gameMap.listOfPeople):
                        peopleHere = gameMap.listOfPeople[index]
                        index += 1
                else:
                        peopleHere = "none"
                description = gameMap.mapOfLocations.map[k] + "\n People here:\n" + peopleHere
                text = font.render(description, 1, (255, 255, 255))
                screen.blit(text, (k.x - text.get_width()/2 - camera.x, k.y - text.get_height()/2 - camera.y))
        pygame.display.flip()



