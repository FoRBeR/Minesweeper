import numpy as np
import pygame
from random import randint

pygame.init()


def generation():
    i = 1
    while i <= bombcnt:
        x = randint(0, ycls - 1)
        y = randint(0, xcls - 1)
        if downarr[x, y] < 9:
            downarr[x, y] = 9
            i += 1
            if (x == 0) & (y == 0):
                downarr[x + 1, y] += 1
                downarr[x + 1, y + 1] += 1
                downarr[x, y + 1] += 1
            elif (x == ycls - 1) & (y == xcls - 1):
                downarr[x - 1, y] += 1
                downarr[x - 1, y - 1] += 1
                downarr[x, y - 1] += 1
            elif (x == ycls - 1) & (y == 0):
                downarr[x - 1, y] += 1
                downarr[x - 1, y + 1] += 1
                downarr[x, y + 1] += 1
            elif (x == 0) & (y == xcls - 1):
                downarr[x + 1, y] += 1
                downarr[x + 1, y - 1] += 1
                downarr[x, y - 1] += 1
            elif (x == 0):
                downarr[x + 1, y] += 1
                downarr[x + 1, y + 1] += 1
                downarr[x + 1, y - 1] += 1
                downarr[x, y - 1] += 1
                downarr[x, y + 1] += 1
            elif (x == ycls - 1):
                downarr[x - 1, y] += 1
                downarr[x - 1, y + 1] += 1
                downarr[x - 1, y - 1] += 1
                downarr[x, y - 1] += 1
                downarr[x, y + 1] += 1
            elif (y == 0):
                downarr[x + 1, y] += 1
                downarr[x - 1, y] += 1
                downarr[x + 1, y + 1] += 1
                downarr[x, y + 1] += 1
                downarr[x - 1, y + 1] += 1
            elif (y == xcls - 1):
                downarr[x + 1, y] += 1
                downarr[x - 1, y] += 1
                downarr[x + 1, y - 1] += 1
                downarr[x, y - 1] += 1
                downarr[x - 1, y - 1] += 1
            else:
                downarr[x + 1, y] += 1
                downarr[x - 1, y] += 1
                downarr[x, y + 1] += 1
                downarr[x, y - 1] += 1
                downarr[x + 1, y + 1] += 1
                downarr[x + 1, y - 1] += 1
                downarr[x - 1, y + 1] += 1
                downarr[x - 1, y - 1] += 1
    for i in range(ycls):
        for j in range(xcls):
            if downarr[i, j] > 9:
                downarr[i, j] = 9


# перерисовка игровой поверхности и меню
def draw():
    menu.blit(flagcounter, flagcounter_rect)
    menu.blit(timer, timer_rect)
    sc.blit(menu, (0, 0))
    for i in range(ycls):
        for j in range(xcls):
            if uparr[i, j] == 1:
                gs.blit(upceil, (j * clg, i * clg))
            elif uparr[i, j] == 2:
                gs.blit(flag, (j * clg, i * clg))
            elif downarr[i, j] == 9:
                gs.blit(bomblose, (j * clg, i * clg))
            else:
                gs.blit(numdict[downarr[i, j]], (j * clg, i * clg))


# определение по какой ячейке нажали, если нажали не на ячейку, возратит -1, -1
def mousepos():
    pos = pygame.mouse.get_pos()
    x = pos[0] - clg
    y = pos[1] - clg - menuY
    x = x // clg
    y = y // clg
    x, y = y, x
    if (ycls - 1 >= x >= 0) & (xcls - 1 >= y >= 0):
        return x, y
    else:
        return -1, -1


# обновление счетчика
def counter_update(count):
    a1 = count // 100
    a2 = count % 100 // 10
    a3 = count % 10
    flagcounter.blit(figures[a1], (counterpos[0], counterpos[1]))
    flagcounter.blit(figures[a2], (counterpos[0] + counterpos[2], counterpos[1]))
    flagcounter.blit(figures[a3], (counterpos[0] + 2 * counterpos[2], counterpos[1]))


# обновление секундомера
def stopwatch(start, now):
    x = timerpos[0]
    y = timerpos[1]
    step = timerpos[2]
    time = now - start
    time = time // 1000
    seconds = time % 60
    minutes = time // 60
    min1 = minutes % 100 // 10
    min2 = minutes % 10
    sec1 = seconds // 10
    sec2 = seconds % 10
    timer.blit(figures[min1], (x, y))
    timer.blit(figures[min2], (x + step, y))
    if sec2 % 2 == 0:
        timer.blit(dots, (x + 2 * step, y))
    else:
        timer.blit(nothing, (x + 2 * step, y))
    timer.blit(figures[sec1], (x + 3 * step, y))
    timer.blit(figures[sec2], (x + 4 * step, y))


bombcnt = 40  # count of bombs
flagcnt = bombcnt  # количество доступных флагов
xcls = 18  # столбцов
ycls = 14  # строк
clg = 32  # large of ceil
uparr = np.ones((ycls, xcls))  # верхний слой 1 - закрытая ячейка, 2 - флаг, 0 - открытая ячейка
downarr = np.zeros((ycls, xcls))  # нижний слой 0 - пустая, 1-8 - цифры 1-8, 9 - бомба
FPS = 30
start_time = 0
game_cont = True  # идет ли игра
firststep = True  # первый ли ход
brown = (150, 75, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
green = (0, 150, 0)
lblue = (0, 191, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
gray = (195, 195, 195)
menuY = 256
XG = clg * (xcls + 2)
YG = clg * (ycls + 2) + menuY

sc = pygame.display.set_mode((XG, YG))
pygame.display.set_caption("Сапер")
pygame.display.set_icon(pygame.image.load('img/programimage.bmp'))
clock = pygame.time.Clock()
gs = pygame.Surface((XG - 2 * clg, YG - 2 * clg - menuY))

frame = pygame.image.load('img/frame.bmp').convert()
sc.blit(frame, (0, menuY))
menu = pygame.image.load('img/menu.bmp').convert()
basesmile_up = pygame.image.load('img/basesmile_up.bmp').convert()
goodend_up = pygame.image.load('img/goodend_up.bmp').convert()
badend_up = pygame.image.load('img/badend_up.bmp').convert()
basesmile_rect = basesmile_up.get_rect(midbottom=(XG // 2, menuY))
goodend_rect = goodend_up.get_rect(midbottom=(XG // 2, menuY))
badend_rect = badend_up.get_rect(midbottom=(XG // 2, menuY))
flagcounter = pygame.image.load('img/score/flagscount.bmp').convert()
flagcounter_rect = flagcounter.get_rect(topright=(XG - clg, clg))
timer = pygame.image.load('img/score/timer.bmp').convert()
timer_rect = timer.get_rect(topleft=(clg, clg))
counterpos = np.array([128, 42, 26])  # куда в счетчике располагать цифры 0 - x, 1 - y, 2 - сдвиг до следующей
timerpos = np.array([102, 42, 26])  # куда в таймере располагать цифры 0 - x, 1 - y, 2 - сдвиг до следующей
menu.blit(flagcounter, flagcounter_rect)
menu.blit(timer, timer_rect)
menu.blit(basesmile_up, basesmile_rect)
sc.blit(menu, (0, 0))

downceil = pygame.image.load('img/downceil.bmp').convert()
bomb = pygame.image.load('img/bomb.png').convert_alpha()
bomb.set_colorkey(white)
bomblose = pygame.Surface((clg, clg))
bomblose.fill(red)
bomblose.blit(bomb, (0, 0))
upceil = pygame.image.load('img/upceil.bmp').convert()
flag = pygame.image.load('img/flag.bmp').convert()
# цифры на поле
num1 = pygame.image.load('img/num1.bmp').convert()
num2 = pygame.image.load('img/num2.bmp').convert()
num3 = pygame.image.load('img/num3.bmp').convert()
num4 = pygame.image.load('img/num4.bmp').convert()
num5 = pygame.image.load('img/num5.bmp').convert()
num6 = pygame.image.load('img/num6.bmp').convert()
num7 = pygame.image.load('img/num7.bmp').convert()
num8 = pygame.image.load('img/num8.bmp').convert()
# цифры для интерфейса
zero = pygame.image.load('img/score/zero.bmp').convert()
one = pygame.image.load('img/score/one.bmp').convert()
two = pygame.image.load('img/score/two.bmp').convert()
three = pygame.image.load('img/score/three.bmp').convert()
four = pygame.image.load('img/score/four.bmp').convert()
five = pygame.image.load('img/score/five.bmp').convert()
six = pygame.image.load('img/score/six.bmp').convert()
seven = pygame.image.load('img/score/seven.bmp').convert()
eight = pygame.image.load('img/score/eight.bmp').convert()
nine = pygame.image.load('img/score/nine.bmp').convert()
dots = pygame.image.load('img/score/dots.bmp').convert()
nothing = pygame.image.load('img/score/nothing.bmp').convert()

numdict = {0: downceil, 1: num1, 2: num2, 3: num3, 4: num4, 5: num5, 6: num6, 7: num7, 8: num8}
figures = {0: zero, 1: one, 2: two, 3: three, 4: four, 5: five, 6: six, 7: seven, 8: eight, 9: nine}
generation()
counter_update(flagcnt)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            x, y = mousepos()
            if (x != -1) & (game_cont == True):
                if (event.button == 1) & (uparr[x, y] != 2):
                    if firststep == True:  # если первый ход, то генерируем пока не будет норм поле
                        while downarr[x, y] == 9:
                            generation()
                        firststep = False
                        start_time = pygame.time.get_ticks()
                    uparr[x, y] = 0
                    if downarr[x, y] == 9:
                        game_cont = False
                        start_time = 0
                        menu.blit(badend_up, badend_rect)
                        sc.blit(menu, (0, 0))
                        uparr = uparr * 0
                if event.button == 3:
                    if (uparr[x, y] == 1) & (flagcnt > 0):
                        uparr[x, y] = 2
                        flagcnt -= 1
                        counter_update(flagcnt)
                    elif uparr[x, y] == 2:
                        uparr[x, y] = 1
                        flagcnt += 1
                        counter_update(flagcnt)
            elif (basesmile_rect.collidepoint(position[0], position[1])):  # если нажали на рестарт
                flagcnt = bombcnt
                counter_update(flagcnt)
                start_time = 0
                stopwatch(0, 0)
                game_cont = True
                firststep = True
                uparr = uparr * 0 + 1
                downarr = downarr * 0
                menu.blit(basesmile_up, basesmile_rect)
                generation()
                draw()
    if (flagcnt == 0) & (uparr.sum() == bombcnt * 2):
        game_cont = False
        start_time = 0
        menu.blit(goodend_up, goodend_rect)
        sc.blit(menu, (0, 0))
    if start_time > 0:
        now_time = pygame.time.get_ticks()
        stopwatch(start_time, now_time)
    draw()
    sc.blit(gs, (clg, clg + menuY))
    pygame.display.update()
    clock.tick(FPS)
