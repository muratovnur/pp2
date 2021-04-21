import pygame, sys
from pygame.locals import *
import random, time

pygame.init()
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = [5, 8, 10, 12, 15]
SCORE = 0
COINS_SCORE = 0
coin_active = False
x = 0
 
#Setting up Fonts
font = pygame.font.Font('freesansbold.ttf', 60)
font_small = pygame.font.Font('freesansbold.ttf', 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("AnimatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(40,SCREEN_WIDTH-40), 0))
 
    def move(self):
        global x
        global SCORE
        self.rect.move_ip(0,SPEED[x])
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            x = random.randint(0,4)
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center = (160, 520))
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("coin.png")
        self.surf = pygame.Surface((48, 48))
        self.rect = self.surf.get_rect(center = (random.randint(40,SCREEN_WIDTH-40), 0))
        
    def move(self):
        self.rect.move_ip(0,7)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
 
#Adding a new User event 
#INC_SPEED = pygame.USEREVENT + 1
#pygame.time.set_timer(INC_SPEED, 1000)

SPAWN_COIN = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_COIN, random.randint(4000,7000))
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        #if event.type == INC_SPEED:
            #SPEED += 0.5
        if event.type == SPAWN_COIN:
            coin_active = True
            C1 = Coin()
            coins = pygame.sprite.Group()
            all_sprites.add(C1)
            coins.add(C1)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    coins_collected = font_small.render('Coins: ' + str(COINS_SCORE), True, YELLOW)
    DISPLAYSURF.blit(coins_collected, (310,10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
    
    if coin_active:
        if pygame.sprite.spritecollideany(P1, coins):
            COINS_SCORE += 1
            C1.kill()
            all_sprites.remove(C1)
            coin_active = False
    

    pygame.display.update()
    FramePerSec.tick(FPS)