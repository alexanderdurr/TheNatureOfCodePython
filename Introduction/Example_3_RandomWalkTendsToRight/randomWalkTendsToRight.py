__author__ = 'Timotheus Kampik'
import sys
from random import uniform
#import and init pygame
import pygame
pygame.init()

#create screen
window = pygame.display.set_mode((640, 480))

class Walker():
    #initiate and draw walker
    def __init__(self):
        self.x = int(window.get_width() / 2)
        self.y = int(window.get_height() / 2)
         #draw circle & display
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), 1, 0)
        pygame.display.flip()

    # "move" walker to random direction (right, left, up, down)
    def draw(self):
        self.step()
        #draw circle & display
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), 1, 0)
        pygame.display.flip()

    # randomly choose new direction, but prevent walker from "leaving" screen
    def step(self):
        choice = uniform(0,1)
        # here we have a 28% chance of increasing x
        if 0.28 > choice and self.x < window.get_width():
            self.x += 1
        # here
        elif 0.2 < choice < 21 and self.x > 0:
            self.x -= 1
        elif 21 < choice < 31 and self.y < window.get_height():
            self.y += 1
        elif 31 < choice and self.y > 0:
            self.y -= 1


#create and init new walker object
walker = Walker()


#input handling:
while True:
   walker.draw()
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit(0)
      else:
          print(event)














