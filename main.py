import pygame
from affichage import *
from personnage import *
from time import sleep


scene_combat, scene_menu  = init_scene()

Robert = Personnage()


pygame.init()
PLAY = True

pygame.display.set_caption("Slice 2 Dice")
screen = pygame.display.set_mode([1000, 500])

CURRENT_SCENE = scene_menu
# Run until the user asks to quit
while PLAY:
    # sleep(2)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PLAY = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                CURRENT_SCENE = scene_combat

            if event.key == pygame.K_RIGHT:
                CURRENT_SCENE = scene_menu    



    affiche(screen, CURRENT_SCENE)
    
    affiche_perso(screen, Robert, 1)
    affiche_perso(screen, Robert, 2)
    affiche_perso(screen, Robert, 3)
    affiche_perso(screen, Robert, 4)
    affiche_perso(screen, Robert, 5)
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()