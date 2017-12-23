#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import random
import sys
from tkinter import *

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
master = Tk()
done = False
draw_on = False
last_pos = (0, 0)
color = (255, 128, 0)
radius = 3
r = random.randint(20, 255)
g = random.randint(20, 255)
b = random.randint(20, 255)


def roundline(
    srf,
    color,
    start,
    end,
    radius=1,
    ):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i) / distance * dx)
        y = int(start[1] + float(i) / distance * dy)
        pygame.draw.circle(srf, color, (x, y), radius)


while not done:
    e = pygame.event.wait()

    if e.type == pygame.QUIT:
        done = True
        pygame.quit()
        break

    if done:
        break
    if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
        screen.fill((0, 0, 0))
        print 'cleared'
    if e.type == pygame.MOUSEBUTTONDOWN:
        print e.button
        if e.button == 1:
            print 'drawing'
            color = (r, g, b)
            pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True
            print draw_on
        elif e.button == 3:
            print 'changing'
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            # print ("r" + r + "g" + g + "b" + b)

    if e.type == pygame.MOUSEBUTTONUP:
        draw_on = False
    if e.type == pygame.MOUSEMOTION:
        if draw_on:

            pygame.draw.circle(screen, color, e.pos, radius)
            roundline(screen, color, e.pos, last_pos, radius)
        last_pos = e.pos

    pygame.display.flip()

# pygame.quit()


			