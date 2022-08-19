import pygame
import pygame, sys
from pygame.locals import *
import random
import decimal
import time
import os

def main():
    pygame.init()

    (width,height) = (640,640)

    clock = pygame.time.Clock()

    DISPLAY = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Hacker Escape")

    coolpic = pygame.image.load("hacker2.jpg")
    coolpic = pygame.transform.scale(coolpic, (50, 50))

    pizzapic = pygame.image.load("one.jpg")
    pizzapic = pygame.transform.scale(pizzapic, (50, 50))

    zeropic = pygame.image.load("zero.jpg")
    zeropic = pygame.transform.scale(zeropic, (50, 50))

    virusbomb = pygame.image.load("virusbomb.jpg")
    virusbomb = pygame.transform.scale(virusbomb, (640, 640))

    #-------------------------

    redpercent = pygame.image.load("redpercent.jpg")
    redpercent = pygame.transform.scale(redpercent, (50, 50))

    redat = pygame.image.load("redat.jpg")
    redat = pygame.transform.scale(redat, (50, 50))

    #-----------------

    BOSS1 = pygame.image.load("boss1.jpg")
    BOSS1 = pygame.transform.scale(BOSS1, (100, 100))

    BOSS2 = pygame.image.load("boss2.jpg")
    BOSS2 = pygame.transform.scale(BOSS2, (100, 100))

    black= (0,0,0)

    DISPLAY.fill(black)

    x_pos = 640/2
    y_pos = 640/2
    
    class Enemy:
        xposenemy = 640/2
        yposenemy = 640/2
        def __init__(self, xposenemy, yposenemy):
            self.xposenemy = xposenemy
            self.yposenemy = yposenemy

    class BossEnemy:
        xposboss = random.randint(0, 640 -32)
        yposboss = random.randint(-640, -32)
        def __init__(self, xposboss , yposboss):
            self.xposenemy = xposboss 
            self.yposenemy = yposboss 
            
    bossenemies = []

    enemies = []


    for i in range(5):
        enemies.append(Enemy(random.randint(0, 640 -32), random.randint(-640, -32)))


    #COUNTERS

    playerspeed = 1
    numofenemies = 5
    increasenumber = 1
    chargebar = 0
    timecounter = 0
    hardness = 1 
    enemyspeed = 1
    LEVELCOUNTER = 1
    bossmade = "no"

    #hardness IMPLIMENT HARDNESS (HARDER AS LEVELS COMPLETE)

    ###------------


    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        #basic controls
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if x_pos > 600:
                pass
            if x_pos < 600:
                x_pos = x_pos+3 * playerspeed
        if keys[pygame.K_LEFT]:
            if x_pos < 0:
                pass
            if x_pos > 0:
                x_pos = x_pos-3 * playerspeed   

        if keys[pygame.K_UP]:
            if y_pos < 20:
                pass
            else:
                y_pos = y_pos-3 * playerspeed
        if keys[pygame.K_DOWN]:
            if y_pos > 600:
                pass
            else:
                y_pos = y_pos+3 * playerspeed

        #enemy stuff
        #increase enemies in a way not too fast not too slow 
        (numofenemies) += decimal.Decimal(0.00001)*decimal.Decimal(increasenumber)

        #check to see if they have made it correct time
        if timecounter > 100:
            hardness += 1 
            timecounter = 0

        if hardness == 21:
            #THEN NEXT LEVEL
            enemyspeed += 1
            hardness = 1
            for i in range(hardness):
                enemies.append(Enemy(random.randint(0, 640 -32), random.randint(-640, -32)))

            LEVELCOUNTER += 1
           
        if chargebar != 1001:
            chargebar += 1

        timecounter += 1

        for enemy in enemies:

            if numofenemies > 5:
                numofenemies = numofenemies - 4

            print("amount of enemies = ",len(enemies), "INCREASING BY  =",round(increasenumber,4),"chargebar = ",chargebar,"HARDNESS =", hardness, "LEVEL =", LEVELCOUNTER, x_pos,y_pos )
                
            enemy.yposenemy = enemy.yposenemy + enemyspeed
    
            if enemy.yposenemy > 640:
                enemy.yposenemy = -32
                enemy.xposenemy = random.randint(0,640 - 32)

                for i in range(int(numofenemies)):
                    enemies.append(Enemy(random.randint(0, 640 -32), random.randint(-640, -32)))
                
                increasenumber = decimal.Decimal(1/len(enemies))

                while len(enemies) > 50:
                    enemies = enemies[10:]
                    
            #if u get hit # add boss hit
            if x_pos +32 > enemy.xposenemy and x_pos < enemy.xposenemy + 32 and y_pos +32 > enemy.yposenemy and enemy.xposenemy and y_pos < enemy.yposenemy + 32 and y_pos +32 > enemy.yposenemy:
                x_pos = 640/2 -32/2
                y_pos = 640/2 -32/2

                enemies = []
                chargebar = 0
                playerspeed = 1
                numofenemies = 5
                increasenumber = 1
                chargebar = 0
                timecounter = 0
                hardness = 1 
                enemyspeed = 1
                LEVELCOUNTER = 1
                bossmade == "no"
                bossenemies = []

                for i in range(7):
                    enemies.append(Enemy(random.randint(0, 640 -32), random.randint(-640, -32)))
            
        #make the screen
        DISPLAY.fill(black)
        DISPLAY.blit(coolpic, (x_pos,y_pos))

        #chargebar
        font = pygame.font.SysFont(None, 40)


        if chargebar < 1000:
            chargebartext = font.render (f"chargebar: {int(chargebar/10)}%", True, (0,250,0))
        if chargebar > 1000: 
            chargebartext = font.render (f"chargebar: 100% READY", True, (0,250,0))   

        font2 = pygame.font.SysFont(None, 20)
        font3 = pygame.font.SysFont(None, 22)

        controls = font2.render(f"WASD // (ALT or CTRL + WASD for special moves) // SPACEBAR for VIRUS BOMB",True,(200,100,30))
        levelscreen = font3.render(f"LEVEL = {LEVELCOUNTER}",True,(0,100,70))

        DISPLAY.blit(controls,(0,620))
        DISPLAY.blit(chargebartext, (0,0))
        DISPLAY.blit(levelscreen,(560,620))


        #display enemy and displayign glitching
        for enemy in enemies:
            try:
                odds = random.randint(1*(hardness*500),10000)
            except ValueError:
                odds = 10000
            #THERE IS A GLITCH HERE WHEN HARDNESS GOES OVER 10000 then only glitches so we check odds

            if odds == 10000:
                for i in range(10):
                    DISPLAY.blit(coolpic, (random.randint(0,640), (y_pos)))
                    DISPLAY.blit(coolpic, (random.randint(0,640), (y_pos)))

                    pygame.display.update()

            oddsnumber = random.randint(1,3)
            if oddsnumber > 1:
                DISPLAY.blit(pizzapic, (enemy.xposenemy, enemy.yposenemy))
            if oddsnumber == 1: 
                DISPLAY.blit(zeropic, (enemy.xposenemy, enemy.yposenemy))

            oddsscreen = random.randint(1*hardness,10000)
            if oddsscreen == 10000:
                for i in range (50):
                    x = random.randint(0,1000)
                    y = random.randint(0,1000)
                    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

                        
                    #change pos 
                    screen = pygame.display.set_mode((random.randint(300,800),random.randint(300,800)))
                    pygame.display.update()
                pygame.display.set_mode((640,640))

        #BOSS
        if LEVELCOUNTER > 1: #change when boss appear
            if bossmade == "no":
                for i in range(3):
                    bossenemies.append(BossEnemy(random.randint(0, 640 -32), random.randint(-640, -32)))
            bossmade = "yes"
        #for bossenemy AI

        for boss in bossenemies:
            oddsnumber = random.randint(1,3)
            if oddsnumber > 1:
                DISPLAY.blit(BOSS1, (boss.xposboss, boss.yposboss,))
            if oddsnumber == 1: 
                DISPLAY.blit(BOSS2, (boss.xposboss, boss.yposboss))

            if x_pos < boss.xposboss:
                boss.xposboss = boss.xposboss - 1
            if x_pos > boss.xposboss:
                boss.xposboss = boss.xposboss + 1
        
            
            boss.yposboss = boss.yposboss + 2
            

            if boss.yposboss > 640:
                boss.yposboss = -32
                boss.xposboss = random.randint(0,640 - 32)

            pygame.display.update()
    

        #SPECIAL CONTROLS
        if keys[pygame.K_SPACE]:

            if chargebar > 1000:

                chargebar = 0
                
                for i in range(5):
                    DISPLAY.blit(virusbomb, (0, 0))
                    pygame.display.update()
                time.sleep(2)
                enemies = []
                bossenemies = []
                bossmade == "no"
                
                for i in range(15):
                    enemies.append(Enemy(random.randint(0, 640 -32), random.randint(-640, -32)))

        pygame.display.update()


        if keys[pygame.K_LALT]:
    
            if chargebar > 100:
                oldenemyspeed = enemyspeed
                oldplayerspeed = playerspeed
                for i in range(1000):
                    playerspeed = 0.05
                    
                    enemyspeed = 0
                    if keys[pygame.K_RIGHT]:
                        if x_pos > 600:
                            print("too far")
                        if x_pos < 600:
                            DISPLAY.blit(coolpic, ((x_pos),random.randint(0,640)))
                            x_pos = x_pos+3 * playerspeed
                    if keys[pygame.K_LEFT]:
                        if x_pos < 0:
                            pass
                        if x_pos > 0:
                            DISPLAY.blit(coolpic, ((x_pos),random.randint(0,640)))
                            x_pos = x_pos-3 * playerspeed   

                    if keys[pygame.K_UP]:
                        if y_pos < 20:
                            pass
                        else:
                            y_pos = y_pos-3 * playerspeed
                            DISPLAY.blit(coolpic, (random.randint(0,640), (y_pos)))
                    if keys[pygame.K_DOWN]:
                        if y_pos > 600:
                            pass
                        else:
                            y_pos = y_pos+3 * playerspeed
                            DISPLAY.blit(coolpic, (random.randint(0,640), (y_pos)))
                    pygame.display.update()
                    

                chargebar = chargebar -100
                enemyspeed = oldenemyspeed
                playerspeed = oldplayerspeed

        if keys[pygame.K_LCTRL]:
    
            if chargebar > 100:
                oldenemyspeed = enemyspeed
                oldplayerspeed = playerspeed
                for i in range(10):
                    for enemy in enemies:
                    
                        if keys[pygame.K_RIGHT]:
                            if x_pos > 600:
                                print("too far")
                            if x_pos < 600:
                                enemy.xposenemy= enemy.xposenemy+3 * enemyspeed
                        if keys[pygame.K_LEFT]:
                            if x_pos < 0:
                                pass
                            if x_pos > 0:
                                enemy.xposenemy= enemy.xposenemy-3 * enemyspeed 

                        if keys[pygame.K_UP]:
                            if enemy.yposenemy < 20:
                                pass
                            else:
                                enemy.yposenemy= enemy.yposenemy-3 * enemyspeed
                                
                        if keys[pygame.K_DOWN]:
                            if y_pos > 600:
                                pass
                            else:
                                enemy.yposenemy= enemy.yposenemy+3 * enemyspeed

                            oddsnumber = random.randint(1,3)
                        if oddsnumber > 1:
                            DISPLAY.blit(redat, (enemy.xposenemy, enemy.yposenemy))
                        if oddsnumber == 1: 
                            DISPLAY.blit(redpercent, (enemy.xposenemy, enemy.yposenemy))

                        if chargebar > 0:
                            chargebar = chargebar - 0.1
                        pygame.display.update()
    
main()