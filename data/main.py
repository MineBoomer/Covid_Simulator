import pygame
from pygame.locals import *
try:
    from data.preload import *
except:
    from preload import *
from random import randint
from pygame.time import Clock, wait
from pylab import *

grille = []

def ImportNiveaux(niveau):
    global grille
    fichier = f"data/Niveaux/Niv{niveau}.txt"
    with open(fichier, 'r') as f:
        grille=[[lettre for lettre in ligne if lettre!="\n"] for ligne in f]
    return grille

def affichage_game():
    global health, grille, bg, infected
    blit(bg,(0,0))
    for i in range(40):
        for o in range(40):
            if grille[i][o]=='i': # Infected
                blit(infected, (i*15,o*15))
            elif grille[i][o]=='v': # Immune
                blit(immune,(i*15,o*15))
            elif grille[i][o]=='0': # Health
                blit(health,(i*15,o*15))
    pygame.display.flip()

def affichage_menu():
    blit(menu,(0,0))
    pygame.display.flip()

def Infect():
    rndm = randint(1,39)
    for i in range(rndm,randint(rndm,39),1):
        for o in range(randint(1,39),39,1):
            if grille[i][o]=='i':
                alea = randint(1,8)
                if alea == 1:
                    if grille[i+1][o]=='0':
                        grille[i+1][o]='i'
                        return
                if alea == 2:
                    if grille[i-1][o]=='0':
                        grille[i-1][o]='i'
                        return
                if alea == 3:
                    if grille[i][o+1]=='0':
                        grille[i][o+1]='i'
                        return
                if alea == 4:
                    if grille[i][o-1]=='0':
                        grille[i][o-1]='i'
                        return
                if alea == 5:
                    if grille[i+1][o+1]=='0':
                        grille[i+1][o+1]='i'
                        return
                if alea == 6:
                    if grille[i+1][o-1]=='0':
                        grille[i+1][o-1]='i'
                        return
                if alea == 7:
                    if grille[i-1][o+1]=='0':
                        grille[i-1][o+1]='i'
                        return
                if alea == 8:
                    if grille[i-1][o-1]=='0':
                        grille[i-1][o-1]='i'
                        return

def Immune():
        rndm = randint(1,39)
        for i in range(rndm,randint(rndm,39),1):
            for o in range(randint(1,39),39,1):
                if grille[i][o]=='v':
                    alea = randint(1,8)
                    if alea == 1:
                        if grille[i+1][o]=='i':
                            grille[i+1][o]='v'
                            return
                    if alea == 2:
                        if grille[i-1][o]=='i':
                            grille[i-1][o]='v'
                            return
                    if alea == 3:
                        if grille[i][o+1]=='i':
                            grille[i][o+1]='v'
                            return
                    if alea == 4:
                        if grille[i][o-1]=='i':
                            grille[i][o-1]='v'
                            return
                    if alea == 5:
                        if grille[i+1][o+1]=='i':
                            grille[i+1][o+1]='v'
                            return
                    if alea == 6:
                        if grille[i+1][o-1]=='i':
                            grille[i+1][o-1]='v'
                            return
                    if alea == 7:
                        if grille[i-1][o+1]=='i':
                            grille[i-1][o+1]='v'
                            return
                    if alea == 8:
                        if grille[i-1][o-1]=='i':
                            grille[i-1][o-1]='v'
                            return

def Health():
    ff = randint(1,4)
    if ff == 1:
        rndm = randint(1,39)
        for i in range(rndm,randint(rndm,39),1):
            for o in range(randint(1,39),39,1):
                if grille[i][o]=='0':
                    alea = randint(1,8)
                    if alea == 1:
                        if grille[i+1][o]=='v':
                            grille[i+1][o]='0'
                            return
                    if alea == 2:
                        if grille[i-1][o]=='v':
                            grille[i-1][o]='0'
                            return
                    if alea == 3:
                        if grille[i][o+1]=='v':
                            grille[i][o+1]='0'
                            return
                    if alea == 4:
                        if grille[i][o-1]=='v':
                            grille[i][o-1]='0'
                            return
                    if alea == 5:
                        if grille[i+1][o+1]=='v':
                            grille[i+1][o+1]='0'
                            return
                    if alea == 6:
                        if grille[i+1][o-1]=='v':
                            grille[i+1][o-1]='0'
                            return
                    if alea == 7:
                        if grille[i-1][o+1]=='v':
                            grille[i-1][o+1]='0'
                            return
                    if alea == 8:
                        if grille[i-1][o-1]=='v':
                            grille[i-1][o-1]='0'
                            return

allowInfect = True
def randInfect():
    global allowInfect, immuneStart
    if allowInfect == True:
        immuneStart = [randint(0,39),randint(0,39)]
        grille[immuneStart[0]][immuneStart[1]]='i'
        allowInfect = False

statlistx = []
statlistH = []
statlistI = []
statlistV = []

updCount = 0
def stats():
    global updCount
    statsH = 0
    statsI = 0
    statsV = 0
    updCount += 1
    for i in range(40):
        for o in range(40):
            if grille[i][o]=='i': # Infected
                statsI += 1
            elif grille[i][o]=='v': # Immune
                statsV += 1
            elif grille[i][o]=='0': # Health
                statsH += 1
    Hp = statsH*100/1600
    Ip = statsI*100/1600
    Vp = statsV*100/1600
    print(f"----- Update {updCount} -----")
    print(f"Bonne santé : {statsH} ({Hp}%)")
    print(f"Infécté(s) : {statsI} ({Ip}%)")
    print(f"Immunisé(s) : {statsV} ({Vp}%)")
    if updCount < 10:
        print("--------------------")
    elif updCount < 100:
        print("---------------------")
    else: print("----------------------")
    print("")

    fichier = "data/Stat_info.txt"
    if updCount == 1:
        f = open(fichier, 'w+')
    else:
        f =open(fichier, 'a')
    f.write(f"----- Update {updCount} -----")
    f.write("\n")
    f.write(f"Bonne santee : {statsH} ({Hp}%)")
    f.write("\n")
    f.write(f"Infecte(s) : {statsI} ({Ip}%)")
    f.write("\n")
    f.write(f"Immunise(s) : {statsV} ({Vp}%)")
    f.write("\n")
    if updCount < 10:
        f.write("--------------------")
    elif updCount < 100:
        f.write("---------------------")
    else: f.write("----------------------")
    f.write("\n")
    f.write("\n")
    f.close()
    statlistx.append(updCount)
    statlistH.append(statsH)
    statlistI.append(statsI)
    statlistV.append(statsV)

count = 0
upd = 0
def clear():
    global count, upd, updCount, allowInfect
    for i in range(40):
        for o in range(40):
            if grille[i][o]=='i': # Infected
                grille[i][o] = '0'
            elif grille[i][o]=='v': # Immune
                grille[i][o] = '0'
    count = 0
    upd = 0
    updCount = 0
    allowInfect = True
    randInfect()

ImportNiveaux(1)

clock = pygame.time.Clock()


statlist = [statlistx,statlistH,statlistI,statlistV]

open_screen = True
open_menu = True
open_game = False

while open_screen == True:
    while open_menu == True:
        affichage_menu()
        for event in pygame.event.get():
            if event.type == QUIT:
                open_menu = False
                open_screen = False
        if event.type == KEYDOWN:
            if event.key != K_ESCAPE:
                open_menu = False
                open_game = True
                clear()
            if event.key == K_ESCAPE:
                open_menu = False
                open_screen = False
        if event.type == MOUSEBUTTONDOWN:
            x_click = event.pos[0]
            y_click = event.pos[1]
            if 540 <= x_click <=600 and 530 <= y_click <= 600:
                open_menu = False
                open_screen = False
    while open_game == True:
        affichage_game()
        randInfect()
        for event in pygame.event.get():
            if event.type == QUIT:
                open_game = False
                open_menu = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                open_game = False
                open_menu = True
                wait(250)
        Infect()
        Immune()
        Health()
        count += 1
        if count >= 500 and count <= 1199:
            grille[immuneStart[0]][immuneStart[1]]='v'
        if count >= 1200 and count <= 1500:
            grille[immuneStart[0]][immuneStart[1]]='0'
        upd += 1
        if upd >= 150:
            stats()
            upd = 0
        clock.tick(100)


plot(statlist[0], statlist[1], color = 'g', label = "N")
plot(statlist[0], statlist[2], color = 'm', label = "Inféctés")
plot(statlist[0], statlist[3], color = 'k', label = "Immunisés")
legend()