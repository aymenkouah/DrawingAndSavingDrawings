#Made by: Kouah Mohammed Aymen
#Computer science student at "National Computer science Engineering School, Algiers (ESI)"
#E-mail: jm_kouah@esi.dz
#Github: https://github.com/aymenkouah
#Requires installing "pygame" 
#https:\\pygame.org
#Open the read_me file for more info and the using method

#To change the scale, change the "zoom" variable (decrease the number to zoom in)

import pygame
from math import floor
import random


class grid():
    def __init__(self, height, width, divi):
        self.vert = floor(float(height) / divi)
        self.hor = floor(float(width) / divi)
        self.divi = divi
        self.lis = []
        for i in range(self.hor):
            for k in range(self.vert):
                self.lis.append([i*divi, k*divi, 0])

    def draw(self, window):
        for i in range(len(self.lis)):
            if self.lis[i][2] > 0:
                pygame.draw.rect(
                    window, (255, 0, 0), (self.lis[i][0], self.lis[i][1], self.divi, self.divi))
            pygame.draw.rect(
                window, (255), (self.lis[i][0], self.lis[i][1], self.divi, self.divi), 1)

    def update(self, pos):
        for elem in range(len(self.lis)):
            if self.lis[elem][0] <= pos[0] <= self.lis[elem][0]+self.divi and self.lis[elem][1] <= pos[1] <= self.lis[elem][1]+self.divi:
                self.lis[elem][2] += 1
                self.lis[elem+1][2] += 1
                self.lis[elem-1][2] += 1
                self.lis[elem+self.vert][2] += 1
                self.lis[elem-self.vert][2] += 1
                self.lis[elem+self.vert-1][2] += 1
                self.lis[elem-self.vert-1][2] += 1
                self.lis[elem+self.vert+1][2] += 1
                self.lis[elem-self.vert+1][2] += 1

    def reset(self, window):
        window.fill((0, 0, 0))
        for i in range(len(self.lis)):
            self.lis[i][2] = 0
            pygame.draw.rect(
                window, (255), (self.lis[i][0], self.lis[i][1], self.divi, self.divi), 1)


width = 1100
height = 800
zoom = 10

pygame.init()
pygame.display.set_caption('Crash!')
window = pygame.display.set_mode((width, height))
running = True
i = 0
back = grid(height, width, zoom)
# Draw Once

Rectplace = pygame.draw.rect(window, (0, 0, 0), (0, 0, width, height))
# Main Loop
while running:
    # Mouse position and button clicking.^
    back.draw(window)
    pos = pygame.mouse.get_pos()
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    # Check if the rect collided with the mouse pos
    # and if the left mouse button was pressed.
    if Rectplace.collidepoint(pos) and pressed1:
        i += 1
        pos = pygame.mouse.get_pos()
        print("You have opened a chest! {}".format(i))
        back.update(pos)

    # Quit pygame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                back.reset(window)
            if event.key == pygame.K_DOWN:
                name = str(random.randint(15, 100000))+'.jpg'
                pygame.image.save(window, name)

    pygame.display.update()
