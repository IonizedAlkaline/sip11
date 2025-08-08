import pygame
import random
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("UFO.png")
pygame.display.set_icon(icon)
playerImage= pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change=0
def player(x,y):
    screen.blit(playerImage,(x,y))
enemyImage= []
enemyX = []
enemyY =[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies = 5
for _i in range(num_of_enemies):
    enemyImage.append(pygame.image.load("Enemy.png"))
enemyX.append(random.randint(0,800))
enemyY.append(random.randint(50,150))
enemyX_change=0.3
enemyY_change=40
def enemy(x,y,i):
    screen.blit(enemyImage[i],(x,y))
BulletImg=pygame.image.load("Bullet.png")
BulletX = 0
BulletY=480
BulletX_change = 0
BulletY_change = 5
Bullet_State = 'ready'
score_value=0
font=pygame.font.Font(None,32)
textX = 10
textY = 10

over_font=pygame.font.Font(None,64)
def show_score(x,y):
    score = font.render("Score: " +str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over_text=over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))
done = True
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-0.1
            if event.key==pygame.K_RIGHT:
                playerX_change=0.1    
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change = 0 
    screen.fill((255,0,0))
    if playerX<=0:
        playerX = 0
    elif playerX>=736:
        playerX=736
    playerX+=playerX_change
    player(playerX,playerY)
    for i in range(num_of_enemies):
        if enemyX[i]<=0:
            enemyX_change[i]=0.3
            enemyY+=enemyY_change
        elif enemyX[i]>=736:
            enemyX[i]=-0.3
            enemyY[i]=enemyY[i]+enemyY_change
            enemyX[i]=enemyX[i]+enemyX_change
    enemy(enemyX,enemyY)
    pygame.display.update() 