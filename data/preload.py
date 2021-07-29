import pygame
from pygame.locals import *

pygame.init()

res = (600,600)

screen = pygame.display.set_mode(res)
pygame.display.set_caption("Infection Sim")

loadImg = pygame.image.load
blit = screen.blit

menu = loadImg("data/images/menu.png")
bg = loadImg("data/images/background.png")
health = loadImg("data/images/healthy.png")
infected = loadImg("data/images/infected.png")
immune = loadImg("data/images/immune.png")