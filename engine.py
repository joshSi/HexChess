#!/usr/bin/env python3
import pygame
pygame.init()

board = (6*[0], 7*[0], 8*[0], 9*[0], 10*[0], 11*[0], 10*[0], 9*[0], 8*[0], 7*[0], 6*[0])
run = True

def draw_game():
    win = pygame.display.set_mode((456, 352))
    win.fill((0,0,0))
    HexMap.draw_map(win, 28, 128)
    pygame.display.update()

class HexMap:

    def draw_map(Surface, off_x, off_y):
        for i, col in enumerate(board):
            for j, piece in enumerate(col):
                HexMap.draw_hex(Surface, i*40+off_x, j*32+off_y-len(col)*16+64)

    def draw_hex(Surface, x, y):
        pygame.draw.polygon(Surface, (255,255,255), [(x-28,y),(x-12,y+16),(x+12,y+16),(x+28,y),(x+12,y-16),(x-12,y-16)], 1)

while run:
    pygame.time.delay(1)
    draw_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
pygame.quit()