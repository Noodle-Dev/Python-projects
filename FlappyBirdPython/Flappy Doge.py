import pygame, sys, time, random
from colorama import Fore
from pygame.locals import *

pygame.init()

width = 500
height = 700

pygame.display.set_caption('el Flapi birs pirata')
win = pygame.display.set_mode((width, height))
fps = pygame.time.Clock()

#Img
BgImg = pygame.image.load("back.png").convert()
playerImg = pygame.image.load("Player.png").convert_alpha()
topPipe = pygame.image.load("ObsTop.png").convert_alpha()
DownPipe = pygame.image.load("ObsDown.png").convert_alpha()
#Sounds
sonido = pygame.mixer.Sound('Jump.wav')
winSonido = pygame.mixer.Sound('WinSound.wav')

def pipeRanPos():
    pipeRR = [random.randint(200, (height/2)-30), random.randint((height/2)+20, height-200)]
    return pipeRR

def gameOver():
    win.fill((157,0,0))

def main():
    #playerMain
    score = 0
    playerPos = [100, 350]
    gravity = 0.8
    speed = 0
    jump = -23.5
    #tube main
    pipePos = 700
    pipeWidht = 700
    pipeHeight = pipeRanPos()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    speed = 0
                    sonido.play()
                    speed += jump

        speed += gravity
        speed *= 0.95
        playerPos[1] += speed

        if pipePos >= -10:
            pipePos -= 5
        else:
            pipePos = 700
            pipeHeight = pipeRanPos()
            winSonido.play()
            score += 1

        win.fill((76,134,145))
        win.blit(BgImg, [0, 0])
        #player
        win.blit(playerImg, (int(playerPos[0]), int(playerPos[1])))

        win.blit(topPipe, (pipePos, -pipeHeight[0]))
        win.blit(DownPipe, (pipePos, pipeHeight[1]))

        if playerPos[1] <= pipeHeight[0] or playerPos[1] >= pipeHeight[1]:
            if playerPos[0] in list(range(pipePos, pipePos+pipeWidht)):
                gameOver()
                print(Fore.GREEN +"--------")
                print(Fore.RED + "Perdiste")
                print(Fore.CYAN + f"Puntaje {score}")
                print(Fore.GREEN +"--------")
                print("")

        if playerPos[1] >= height:
            playerPos[1] = height
            speed = 0
        elif playerPos[1] <= 0:
            playerPos[1] = 0
            speed = 0

        pygame.display.flip()
        fps.tick(60)
main()
pygame.quit()
