import pygame
import sys
from megaminx import *
from megaminxSaveManager import SaveManager
from megaminxScrambler import MegaminxScrambler

pygame.init()
clock = pygame.time.Clock()

programIcon = pygame.image.load("../res/minx.png")
pygame.display.set_icon(programIcon)
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("pyMegaminx")

sm = SaveManager()

minx = sm.loadData()
bg_color = pygame.Color("grey12")

while True:
    screen.fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sm.saveData(minx)
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_y]:
                if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    minx = minx.move_y_prime()
                else:
                    minx = minx.move_y()
            if keys[pygame.K_z]:
                if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    minx = minx.move_z_prime()
                else:
                    minx = minx.move_z()
            if keys[pygame.K_u]:
                if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    minx = minx.move_U_prime()
                else:
                    minx = minx.move_U()
            if keys[pygame.K_r]:
                if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    minx = minx.move_R_prime()
                elif pygame.key.get_mods() & pygame.KMOD_LALT:
                    minx = minx.move_AR_prime()
                elif pygame.key.get_mods() & pygame.KMOD_RALT:
                    minx = minx.move_AR()
                else:
                    minx = minx.move_R()
            if keys[pygame.K_l]:
                if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    minx = minx.move_L_prime()
                elif pygame.key.get_mods() & pygame.KMOD_LALT:
                    minx = minx.move_AL_prime()
                elif pygame.key.get_mods() & pygame.KMOD_RALT:
                    minx = minx.move_AL()
                else:
                    minx = minx.move_L()
            if keys[pygame.K_f]:
                if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    minx = minx.move_F_prime()
                else:
                    minx = minx.move_F()
            if keys[pygame.K_d]:
                if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    minx = minx.move_DL_prime()
                elif pygame.key.get_mods() & pygame.KMOD_LALT:
                    minx = minx.move_D_prime()
                elif pygame.key.get_mods() & pygame.KMOD_RALT:
                    minx = minx.move_D()
                else:
                    minx = minx.move_DL()
            if keys[pygame.K_g]:
                if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    minx = minx.move_DR_prime()
                else:
                    minx = minx.move_DR()
            if keys[pygame.K_b]:
                if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    minx = minx.move_BL_prime()
                else:
                    minx = minx.move_BL()
            if keys[pygame.K_n]:
                if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    minx = minx.move_BR_prime()
                else:
                    minx = minx.move_BR()
            if keys[pygame.K_SPACE]:
                if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    minx = minx.move_RMM()
                else:
                    minx = minx.move_RPP()
            if keys[pygame.K_ASTERISK]:
                if pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    minx = minx.move_DMM()
                else:
                    minx = minx.move_DPP()
            if keys[pygame.K_0]:
                minx = MegaminxScrambler().getScrambledMegaminx(minx)
            if keys[pygame.K_1]:
                minx = Megaminx(full=True)
            if keys[pygame.K_2]:
                sm.saveData(minx)
            if keys[pygame.K_3]:
                minx = sm.loadData()
            if keys[pygame.K_4]:
                minx = minx.multiMove(screen, "U R U' R'")


    minx.drawMegaminx(screen)

    pygame.display.flip()
    clock.tick(60)