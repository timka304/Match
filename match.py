import pgzrun
import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((800, 500))

#Images
subway_surfers = pygame.image.load("subway surfers.png")
ludo = pygame.image.load("ludo.png")
candy_crush = pygame.image.load("candy crush.png")
temple_run = pygame.image.load("temple run.png")

screen.blit(subway_surfers, (100, 100))
screen.blit(temple_run, (100, 200))
screen.blit(ludo, (100, 300))
screen.blit(candy_crush, (100, 400))

#Text

font = pygame.font.SysFont("Arial", (50))
text = font.render("LUDO", True, "Blue")
text2 = font.render("Subway Surfers", True, "Blue")
text3 = font.render("Candy Crush", True, "Blue")
text4 = font.render("Temple Run", True, "Blue")

screen.blit(text, (400, 100))
screen.blit(text2, (400, 200))
screen.blit(text3, (400, 300))
screen.blit(text4, (400, 400))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, "red", (pos), 20, 0)
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            pos2 = pygame.mouse.get_pos()
            pygame.draw.line(screen, "red", (pos), (pos2), 5)
            pygame.draw.circle(screen, "red", (pos2), 20, 0)
            pygame.display.update()

pygame.quit()