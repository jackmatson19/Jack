#week 15: worked on finding game menu and altered settings

# code taken from F-Prime  at https://github.com/f-prime/FlappyBird

#importing libraries
import pygame 
from pygame.locals import *  
import sys
import random
import time

#code typed from youtube video 
#currently not wroking 
#working with another set of code for flappy bird from Github that came with a starting menu 
#goal is to be able to have a main game menu next week 
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)

theme = input("Choose your theme: (space, midevill, star wars, original)")
#class of bird
class FlappyBird:
    def __init__(self):
        #size of playing screen 
        self.screen = pygame.display.set_mode((400, 708))
        #size of images
        self.bird = pygame.Rect(65, 50, 50, 50) 
        if theme == "space": 
            #the background in the game from the folder 'assets'
            self.background = pygame.image.load("assets/background.png").convert()
            #the bird images
            self.birdSprites = [pygame.image.load("assets/1.png").convert_alpha(),
                                pygame.image.load("assets/2.png").convert_alpha(),
                                pygame.image.load("assets/dead.png")]
            #the obstacles in the game from the folder
            self.wallUp = pygame.image.load("assets/bottom.png").convert_alpha()
            self.wallDown = pygame.image.load("assets/top.png").convert_alpha()
        if theme == "original": 
            #the background in the game from the folder 'assets'
            self.background = pygame.image.load("assets/background1.png").convert()
            #the bird images
            self.birdSprites = [pygame.image.load("assets/1.png").convert_alpha(),
                                pygame.image.load("assets/2.png").convert_alpha(),
                                pygame.image.load("assets/dead.png")]
            #the obstacles in the game from the folder
            self.wallUp = pygame.image.load("assets/NObottom.png").convert_alpha()
            self.wallDown = pygame.image.load("assets/NOtop.png").convert_alpha()
        #changes the distance between obstacles  
        self.gap = 140
        self.wallx = 500
        self.birdY = 350
        self.jump = 0
        self.jumpSpeed = 10
        self.gravity = 5
        self.dead = False
        self.sprite = 0 
        self.counter = 0
        self.offset = random.randint(-110, 110)

    def updateWalls(self):
        self.wallx -= 5
        if self.wallx < -80:
            self.wallx = 550
            self.counter += 1
            #wall randomization 
            self.offset = random.randint(-110, 110)

    def birdUpdate(self):
        if self.jump:
            self.jumpSpeed -= 1
            self.birdY -= self.jumpSpeed
            self.jump -= 1
        else:
            #gravity setttings for the bird
            self.birdY += self.gravity
            self.gravity += 0.3
        self.bird[1] = self.birdY
        upRect = pygame.Rect(self.wallx,
                             360 + self.gap - self.offset + 10,
                             self.wallUp.get_width() - 10,
                             self.wallUp.get_height())
        downRect = pygame.Rect(self.wallx,
                               0 - self.gap - self.offset - 10,
                               self.wallDown.get_width() - 10,
                               self.wallDown.get_height())
        if upRect.colliderect(self.bird):
            self.dead = True
        if downRect.colliderect(self.bird):
            self.dead = True
        if not 0 < self.bird[1] < 720:
            self.bird[1] = 50
            self.birdY = 50
            self.dead = False
            self.counter = 0
            self.wallx = 400
            self.offset = random.randint(-110, 110)
            self.gravity = 5

    def run(self):
        clock = pygame.time.Clock()
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 50)
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not self.dead:
                    self.jump = 17
                    self.gravity = 5
                    self.jumpSpeed = 12
#variation of the walls 
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.wallUp,
                             (self.wallx, 360 + self.gap - self.offset))
            self.screen.blit(self.wallDown,
                             (self.wallx, 0 - self.gap - self.offset))
            self.screen.blit(font.render(str(self.counter),
                                         -1,
                                         (255, 255, 255)),
                             (200, 50))
            if self.dead:
                self.sprite = 2
            elif self.jump:
                self.sprite = 1
            self.screen.blit(self.birdSprites[self.sprite], (70, self.birdY))
            if not self.dead:
                self.sprite = 0
            self.updateWalls()
            self.birdUpdate()
            pygame.display.update()

if __name__ == "__main__":
    FlappyBird().run()