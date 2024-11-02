import pygame
import sys
import random
import os



def b_animation():
    global bsx, bsy, p_score, po_score, score_time
    ball.x += bsx
    ball.y += bsy

    if ball.top <= 0 or ball.bottom >= screenH:
        bsy *= -1
    if ball.left <= 0:
        p_score += 1
        score_time = pygame.time.get_ticks()
    if ball.right >= screenW:
        po_score += 1
        score_time = pygame.time.get_ticks()
    if ball.colliderect(player) and bsx > 0:
        if abs (ball.right - player.left) < 10:
            bsx *= -1
        elif abs (ball.bottom - player.top) < 10 and bsy > 0:
            bsy *= -1
        elif abs (ball.top - player.bottom) < 10 and bsy < 0:
            bsy *= -1
    if ball.colliderect(playerO) and bsx < 0:
        if abs (ball.left - playerO.right) < 10:
            bsx *= -1
        elif abs (ball.bottom - playerO.top) < 10 and bsy > 0:
            bsy *= -1
        elif abs (ball.top - playerO.bottom) < 10 and bsy < 0:
            bsy *= -1

def p_animation():
    player.y += ps
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screenH:
        player.bottom = screenH
def pO_animation():
    if playerO.top < ball.y:
        playerO.top += pso
    if playerO.bottom > ball.y:
        playerO.bottom -= pso
    if playerO.top <= 0:
        playerO.top = 0
    if playerO.bottom >= screenH:
        playerO.bottom = screenH
def b_restart():
    global bsy, bsx, score_time

    now_time = pygame.time.get_ticks()
    ball.center = (screenW /2, screenH /2)

    if now_time - score_time < 700:
        numer_3 = game_text.render("3", False, grey)
        screen.blit(numer_3, (screenW/2 - 10, screenH/2 + 20))
    if 700< now_time - score_time < 1400:
        numer_2 = game_text.render("2", False, grey)
        screen.blit(numer_2, (screenW/2 - 10, screenH/2 + 20))
    if 1400 < now_time - score_time < 2100:
        numer_1 = game_text.render("1", False, grey)
        screen.blit(numer_1, (screenW/2 - 10, screenH/2 + 20))
    if now_time - score_time < 2100:
        bsx, bsy = 0, 0
    else:
        bsy = 7 * random.choice((1,-1))
        bsx = 7 * random.choice((1, -1))
        score_time = None

pygame.init()
clock = pygame.time.Clock()
screenW = 1100
screenH = 680

icon = pygame.image.load('Images/Single.png')

screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption('PingPong Singleplayer')
pygame.display.set_icon(icon)

ball = pygame.Rect(screenW/2 -15,screenH/2 -15, 15, 15)
player  = pygame.Rect(screenW - 20, screenH/2 -70, 10, 140)
playerO  = pygame.Rect(10, screenH/2 -70, 10, 140)

backcolor = (26, 170, 0)
grey = (200,200,200)
red = (250, 34 ,10)
black = (0, 0, 0)
white = (250, 250, 250)

bsx = 7 * random.choice((1, -1))
bsy = 7 * random.choice((1, -1))
ps = 0
pso = 15

p_score = 0
po_score = 0
game_text = pygame.font.Font("C:\Windows\Fonts\BRADHITC.ttf", 32)
score_time = True

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            os.system("PingPong.py")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                ps += 7
            if event.key == pygame.K_UP:
                ps -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                ps -= 7
            if event.key == pygame.K_UP:
                ps += 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                os.system("PingPong.py")

    b_animation()
    p_animation()
    pO_animation()
    

    screen.fill(backcolor)
    pygame.draw.rect(screen, red, player)
    pygame.draw.rect(screen, black, playerO)
    pygame.draw.aaline(screen, grey, (screenW/2, 0), (screenW/2, screenH))
    pygame.draw.ellipse(screen, white, ball)

    if score_time:
        b_restart()

    p_font = game_text.render(f'{p_score}', False, grey)
    screen.blit(p_font, (565, 200))
    po_font = game_text.render(f'{po_score}', False, grey)
    screen.blit(po_font, (510, 200))

    pygame.display.flip()
    clock.tick(80)