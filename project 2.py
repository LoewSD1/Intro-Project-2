# Card Game Project 2
# Seth Loew and Zared Hollabaugh 

#import the necessary libraries
import pygame, random, sys
from pygame.locals import *

#colors
black = (0,0,0)
orange = (255, 128, 0)
green = (34,139,34)
brown = (136, 69, 19)

#variables (opp_score is the your score and comp_score is my score)
opp_Score= 0
comp_Score = 0
mouse_Clicked = False

#initialize pygame
pygame.init()

displaySurf = pygame.display.set_mode((600, 500))

pygame.display.set_caption('Card War')

#images in the game that are permanent
swordsImg = pygame.image.load('swords.png')
card_backImg = pygame.image.load('back.png')

displaySurf.fill(green)

#make the text
fontObj = pygame.font.SysFont('elephant', 32)
textSurf = fontObj.render('Card              War', True, brown, green)
textRect = textSurf.get_rect()
textRect.center = (300, 115)
displaySurf.blit(textSurf, textRect)

fontObj2 = pygame.font.SysFont('times', 12)
textSurf2 = fontObj2.render('Your Score: ' + str(opp_Score), True, black, green)
textRect2 = textSurf2.get_rect()
textRect2.center = (200, 200)
displaySurf.blit(textSurf2, textRect2)

fontObj3 = pygame.font.SysFont('times', 12)
textSurf3 = fontObj3.render('My Score: ' + str(comp_Score), True, black, green)
textRect3 = textSurf3.get_rect()
textRect3.center = (400, 200)
displaySurf.blit(textSurf3, textRect3)

#refresh the screen
pygame.display.update()

#game loop (means this will never become false and will always run
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()   #use only inside pygame
        #if event.type == MOUSEBUTTONUP:
         #   mouse_Clicked = True
    displaySurf.blit(swordsImg, (250, 50))
    displaySurf.blit(card_backImg, (400, 215))
    displaySurf.blit(card_backImg, (150, 215))

    #if mouse_Clicked == True:
        
    pygame.display.update()

    
