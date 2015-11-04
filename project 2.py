# Card Game Project 2
# Seth Loew and Zared Hollabaugh 

#import the necessary libraries
import pygame, random, sys, time
import string
from pygame.locals import *

#make the card class
class Card:
    def __init__(self, card):
        self.card = card
        self.value = checkValue(card)

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
    elif(str(card)[0] == '1'):
        return 9
    elif(str(card)[0] == 'j'):
        return 10
    elif(str(card)[0] == 'q'):
        return 11
    elif(str(card)[0] == 'k'):
        return 12
    elif(str(card)[0] == 'a'):
        return 13

def updatePlayer(playImg, playCard):
    playCard = playerCards.pop()
    playImg = pygame.image.load(playCard.card)
    thingsToReturn = [playImg, playCard]
    return thingsToReturn

def updateComputer(compImg, compCard):
    compCard = computerCards.pop()
    compImg = pygame.image.load(compCard.card)
    thingsToReturn = [compImg, compCard]
    return thingsToReturn

def war(compImg, compCard, playImg, playCard):
    for x in range (0,4):
        playCard = playerCards.pop()
        compCard = computerCards.pop()

    playImg = pygame.image.load(playCard.card)
    compImg = pygame.image.load(compCard.card)

    thingsToReturn =[playImg, compImg, playCard, compCard]

    return thingsToReturn

def gameOver():
    pygame.draw.rect(displaySurf, white, (48, 48, 500, 400))
    fontObj4 = pygame.font.SysFont('times', 35)
    textSurf4 = fontObj4.render('Game Over', True, black, white)
    textRect4 = textSurf4.get_rect()
    textRect4.center = (300, 200)
    displaySurf.blit(textSurf4, textRect4)
    if(playerScore > compScore):
        fontObj5 = pygame.font.SysFont('times', 35)
        textSurf5 = fontObj5.render('You Won!!!', True, black, white)
        textRect5 = textSurf5.get_rect()
        textRect5.center = (300, 250)
        displaySurf.blit(textSurf5, textRect5)
    elif(playerScore < compScore):
        fontObj6 = pygame.font.SysFont('times', 35)
        textSurf6 = fontObj6.render('Sorry, Computer won :(', True, black, white)
        textRect6 = textSurf6.get_rect()
        textRect6.center = (300, 250)
        displaySurf.blit(textSurf6, textRect6)
    else:
        fontObj7 = pygame.font.SysFont('times', 35)
        textSurf7 = fontObj7.render('It was a tie', True, black, white)
        textRect7 = textSurf7.get_rect()
        textRect7.center = (300, 250)
        displaySurf.blit(textSurf7, textRect7)
    fontObj8 = pygame.font.SysFont('times', 35)
    textSurf8 = fontObj8.render('Click here to play again', True, black, white)
    textRect8 = textSurf8.get_rect()
    textRect8.center = (300, 300)
    displaySurf.blit(textSurf8, textRect8)
    pygame.display.update()
    
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
white = (255, 255, 255)

#variables (opp_score is the your score and comp_score is my score)
playerScore= 0
compScore = 0
mouse_Clicked = False
round_Counter = 0
gameComplete = False
drawRectangle = False

#initialize pygame
pygame.init()

displaySurf = pygame.display.set_mode((600, 600))

pygame.display.set_caption('Card War')

#images in the game that are permanent
swordsImg = pygame.image.load('swords.png')
card_backImg = pygame.image.load('back.png')

displaySurf.fill(green)

clicked = 0

#playerImg = pygame.image.load(playerCards.pop().card)
#computerImg = pygame.image.load(computerCards.pop().card)
playerImg = "a"
computerImg = "b"

compCard = Card
playerCard = Card

#variable to make sure we only register 1 click
isMouseDown = 0

#refresh the screen
pygame.display.update()

#game loop (means this will never become false and will always run
while True:
    if(gameComplete) == False and drawRectangle == True:
        pygame.draw.rect(displaySurf, green, (48, 48, 500, 400))
        drawRectangle = False

    for event in pygame.event.get():
        if event.type == QUIT:
           pygame.quit()
           sys.exit()   #use only inside pygame
        #if event.type == MOUSEBUTTONUP:
         #   mouse_Clicked = TruefontObj2 = pygame.font.SysFont('times', 12)
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
    
    displaySurf.blit(swordsImg, (250, 50))
    displaySurf.blit(card_backImg, (400, 215))
    displaySurf.blit(card_backImg, (150, 215))

    #check to see if a click has occured. If so, display cards
    if clicked != 0:
        displaySurf.blit(playerImg, (225, 215))
        displaySurf.blit(computerImg, (325, 215))

    if event.type == pygame.MOUSEBUTTONDOWN:
        #covers up any cards that were displayed during a war.

        if(isMouseDown == 0):
            pygame.draw.rect(displaySurf,green,(225,285,175,300))
            round_Counter += 1
            if round_Counter == 26:
                gameComplete = True
                gameOver()
                round_Counter = 0
            elif(round_Counter < 26):
                playerList = updatePlayer(playerImg, playerCard)
                playerImg = playerList[0]
                playerCard = playerList[1]
                computerList = updateComputer(computerImg, compCard)
                computerImg =  computerList[0]
                compCard = computerList[1]
                if(compCard.value > playerCard.value):
                    compScore += 1
                elif(compCard.value < playerCard.value):
                    playerScore += 1
                elif(compCard.value == playerCard.value):
                    if(round_Counter < 22):
                        #returns a list of playImg, compImg, playCard, compCard: in that order
                        #I know this is really bad, but I want to pass things by reference and Python wasn't made that way :'(
                        returnedList = war(computerImg, compCard, playerImg, playerCard)
                        warPlayerImg = returnedList[0]
                        warComputerImg = returnedList[1]
                        playerCard = returnedList[2]
                        compCard = returnedList[3]

                        round_Counter += 5

                        incrementer = 60
                        for x in range (0,3):
                            displaySurf.blit(card_backImg, (225, 225+incrementer))
                            displaySurf.blit(card_backImg, (325, 225+incrementer))
                            incrementer += 60

                        displaySurf.blit(warPlayerImg, (225, 225+incrementer))
                        displaySurf.blit(warComputerImg, (325, 225+incrementer))

                        #adding a comment
                        if(compCard.value > playerCard.value):
                            compScore += 6
                        elif(compCard.value < playerCard.value):
                            playerScore += 6
                        pygame.display.update()
                        
                if gameComplete == True:
                     #create a list of all of the cards
                    allCards = [Card("2c.png"),Card("2d.png"),Card("2h.png"),Card("2s.png"),Card("3c.png"),Card("3d.png"),Card("3h.png"),Card("3s.png"),Card("4c.png"),Card("4d.png"),Card("4h.png"),Card("4s.png"),Card("5c.png"),Card("5d.png"),Card("5h.png"),Card("5s.png"),Card("6c.png"),Card("6d.png"),Card("6h.png"),Card("6s.png"),Card("7c.png"),Card("7d.png"),Card("7h.png"),Card("7s.png"),Card("8c.png"),Card("8d.png"),Card("8h.png"),Card("8s.png"),Card("9c.png"),Card("9d.png"),Card("9h.png"),Card("9s.png"),Card("10c.png"),Card("10d.png"),Card("10h.png"),Card("10s.png"),Card("jc.png"),Card("jd.png"),Card("jh.png"),Card("js.png"),Card("qc.png"),Card("qd.png"),Card("qh.png"),Card("qs.png"),Card("kc.png"),Card("kd.png"),Card("kh.png"),Card("ks.png"),Card("ac.png"),Card("ad.png"),Card("ah.png"),Card("as.png")]
                    random.shuffle(allCards)

                    drawRectangle = True

                    clicked = 0
                    
                    compScore = 0
                    playerScore = 0

                    #create a list of cards for the computer
                    del computerCards
                    computerCards = []
                
                    for x in range (0,25):
                        computerCards.append(allCards[x])
                    #create a list of cards for the player
                    playerCards = []
                    for x in range(26,51):
                        playerCards.append(allCards[x])
                    gameComplete = False
                    pygame.display.update()
        
        isMouseDown = 1
        clicked = 1

    if event.type == pygame.MOUSEBUTTONUP:
        isMouseDown = 0

##    if gameComplete == True:
##
##        if event.type == pygame.MOUSEBUTTONUP and isMouseDown == 0:
##            print("in function")
##             #create a list of all of the cards
##            allCards = [Card("2c.png"),Card("2d.png"),Card("2h.png"),Card("2s.png"),Card("3c.png"),Card("3d.png"),Card("3h.png"),Card("3s.png"),Card("4c.png"),Card("4d.png"),Card("4h.png"),Card("4s.png"),Card("5c.png"),Card("5d.png"),Card("5h.png"),Card("5s.png"),Card("6c.png"),Card("6d.png"),Card("6h.png"),Card("6s.png"),Card("7c.png"),Card("7d.png"),Card("7h.png"),Card("7s.png"),Card("8c.png"),Card("8d.png"),Card("8h.png"),Card("8s.png"),Card("9c.png"),Card("9d.png"),Card("9h.png"),Card("9s.png"),Card("10c.png"),Card("10d.png"),Card("10h.png"),Card("10s.png"),Card("jc.png"),Card("jd.png"),Card("jh.png"),Card("js.png"),Card("qc.png"),Card("qd.png"),Card("qh.png"),Card("qs.png"),Card("kc.png"),Card("kd.png"),Card("kh.png"),Card("ks.png"),Card("ac.png"),Card("ad.png"),Card("ah.png"),Card("as.png")]
##            random.shuffle(allCards)
##
##            drawRectangle = True
##
##            clicked = 0
##            
##            compScore = 0
##            playerScore = 0
##
##            #create a list of cards for the computer
##            del computerCards
##            computerCards = []
##        
##            for x in range (0,25):
##                computerCards.append(allCards[x])
##            #create a list of cards for the player
##            playerCards = []
##            for x in range(26,51):
##                playerCards.append(allCards[x])
##            gameComplete = False
            
    pygame.display.update()



    
