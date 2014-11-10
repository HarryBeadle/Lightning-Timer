#!/usr/bin/env python

## Lightning Timer
## Harry Beadle

# Import Builtins
from time import time
import os

# Import Dependacies
import pygame
pygame.init()

# Variables
button_color = 223, 62, 125
background_color = 200, 200, 200
key_color = 255, 0, 255
white_color = 255, 255, 255

# Constants
## Speeds
c_light = 3e8
c_sound = 331.3
## Scale
scale = 150
scale = 250
## Screen Dimentions
X = Y = int(scale*1.6)

# Pygame Objects
## Screen
sur_screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Lightning Timer")
sur_screen.fill((255,255,255))
## Buttons
btn_thunder = pygame.image.load(os.path.join("assets", "thunder.png")).convert_alpha()
btn_thunder = pygame.transform.smoothscale(btn_thunder, (scale, scale))
btn_lightning = pygame.image.load(os.path.join("assets", "lightning.png")).convert_alpha()
btn_lightning = pygame.transform.smoothscale(btn_lightning, (scale, scale))
btn_blank = pygame.image.load(os.path.join("assets", "blank.png"))
btn_blank = pygame.transform.smoothscale(btn_blank, (scale, scale))
## Fonts
fnt_default = pygame.font.SysFont("sans", scale/6)
## Icon
pygame.display.set_icon(btn_lightning)

# Functions
def input_():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
            if event.key == pygame.K_RETURN:
                return True
            if event.key == pygame.K_SPACE:
                return True

def reset():
    pygame.draw.rect(sur_screen, background_color, (scale/8, scale/8, X-scale/4, Y-scale/4))

def main():
    reset()
    sur_screen.blit(btn_lightning, ((X-scale)/2, (Y-scale)/2))
    pygame.display.flip()
    times = []
    while True:
        keydown = input_()
        if keydown:
            times.append(time())
            reset()
            sur_screen.blit(btn_thunder, ((X-scale)/2, (Y-scale)/2))
            print time()
            pygame.display.flip()
        if len(times) == 2 and keydown:
            distance = str(round(c_sound * (times[1] - times[0]))) + "m"
            times = []
            reset()
            sur_screen.blit(btn_blank, ((X-scale)/2, (Y-scale)/2))
            sur_screen.blit(
                fnt_default.render(
                    distance,
                    1,
                    white_color
                ),
                (
                    (X-fnt_default.size(distance)[0])/2,
                    (Y-fnt_default.size(distance)[1])/2,
                )
            )
            pygame.display.flip()
            while not input_(): pass
            reset()
            sur_screen.blit(btn_lightning, ((X-scale)/2, (Y-scale)/2))
            pygame.display.flip()
    

# Run
if __name__ == '__main__':
    main()