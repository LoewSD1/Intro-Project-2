# Card Game Project 2
# Seth Loew and Zared Hollabaugh 

#import the necessary libraries
import pygame, random, sys
import string
from pygame.locals import *

#determines value of the card. 
def checkValue(card):
    if(str(card)[0] == '2'):
        return 0
    elif(str(card)[0] == '3'):
        return 1
    elif(str(card)[0] == '4'):
        return 2
    elif(str(card)[0] == '5'):
        return 3
    elif(str(card)[0] == '6'):
        return 4
    elif(str(card)[0] == '7'):
        return 5
    elif(str(card)[0] == '8'):
        return 6
    elif(str(card)[0] == '3'):
        return 7
    elif(str(card)[0] == '9'):
        return 8
    elif(str(card)[0] == '10'):
        return 9
    elif(str(card)[0] == 'j'):
        return 10
    elif(str(card)[0] == 'q'):
        return 11
    elif(str(card)[0] == 'k'):
        return 12
    elif(str(card)[0] == 'a'):
        return 13

def updateGame(playImg, compImg, playScore, compScore):
    #get the card objects
    playCard = playerCards.pop()
    compCard = computerCards.pop()
    #load the image
    assert isinstance(playCard.card, object)
    playImg = pygame.image.load(playCard.card)
    compImg = pygame.image.load(compCard.card)
    #determine points
    if(compCard.value > playCard.value):
        compScore += 1
    elif playCard.value > compCard.value :
        playScore += 1
    else :
        return 0

#make the card class
class Card:
    def __init__(self, card):
        self.card = card
        self.value = checkValue(card)

#create a list of all of the cards
allCards = [Card("2c.png"),Card("2d.png"),Card("2h.png"),Card("2s.png"),Card("3c.png"),Card("3d.png"),Card("3h.png"),Card("3s.png"),Card("4c.png"),Card("4d.png"),Card("4h.png"),Card("4s.png"),Card("5c.png"),Card("5d.png"),Card("5h.png"),Card("5s.png"),Card("6c.png"),Card("6d.png"),Card("6h.png"),Card("6s.png"),Card("7c.png"),Card("7d.png"),Card("7h.png"),Card("7s.png"),Card("8c.png"),Card("8d.png"),Card("8h.png"),Card("8s.png"),Card("9c.png"),Card("9d.png"),Card("9h.png"),Card("9s.png"),Card("10c.png"),Card("10d.png"),Card("10h.png"),Card("10s.png"),Card("jc.png"),Card("jd.png"),Card("jh.png"),Card("js.png"),Card("qc.png"),Card("qd.png"),Card("qh.png"),Card("qs.png"),Card("kc.png"),Card("kd.png"),Card("kh.png"),Card("ks.png"),Card("ac.png"),Card("ad.png"),Card("ah.png"),Card("as.png")]
random.shuffle(allCards)

#create a list of cards for the computer
computerCards = []
for x in range (0,25):
    computerCards.append(allCards[x])

#create a list of cards for the player
playerCards = []
for x in range(26,51):
    playerCards.append(allCards[x])

#colors
black = (0,0,0)
orange = (255, 128, 0)
green = (34,139,34)
brown = (136, 69, 19)

#variables (opp_score is the your score and comp_score is my score)
playerScore= 0
compScore = 0
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
textSurf2 = fontObj2.render('Player Score: ' + str(playerScore), True, black, green)
textRect2 = textSurf2.get_rect()
textRect2.center = (200, 200)
displaySurf.blit(textSurf2, textRect2)

fontObj3 = pygame.font.SysFont('times', 12)
textSurf3 = fontObj3.render('Computer Score: ' + str(compScore), True, black, green)
textRect3 = textSurf3.get_rect()
textRect3.center = (400, 200)
displaySurf.blit(textSurf3, textRect3)

clicked = 0

#playerImg = pygame.image.load(playerCards.pop().card)
#computerImg = pygame.image.load(computerCards.pop().card)
playerImg = "a"
computerImg = "b"

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

    #check to see if a click has occured. If so, display cards
    if clicked != 0:
        displaySurf.blit(playerImg, (150, 215))
        displaySurf.blit(computerImg, (400, 215))

    if event.type == pygame.MOUSEBUTTONUP:
        updateGame(playerImg, computerImg, playerScore, compScore)
        clicked = 1

        
    pygame.display.update()


    
