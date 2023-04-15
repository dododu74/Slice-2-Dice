import pygame
from affichage import *
from personnage import *
# from time import sleep
from random import randint


scene_combat, scene_menu  = init_scene()

# On ajoute des personnages à la scène de combat
for i in range (5):
    root = "Images\Sprites\PropsInPixels_16x" + str(randint(1,172)) + ".png"
    scene_combat.ajout_elm(Personnage(root))

for i in range(3):
    root = "Images\Sprites\PropsInPixels_16x70.png"
    scene_combat.ajout_elm(Ennemi(root))

pygame.init()
PLAY = True

pygame.display.set_caption("Slice 2 Dice")
screen = pygame.display.set_mode([1000, 500])

CURRENT_SCENE = scene_combat
# Run until the user asks to quit
while PLAY:
    # sleep(2)
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PLAY = False

        if event.type == pygame.KEYDOWN:
            
            if CURRENT_SCENE.nom == "Combat":
                if event.key == pygame.K_DOWN:
                    CURRENT_SCENE.perso[0][0].vie_baisser(100)


            if event.key == pygame.K_LEFT:
                CURRENT_SCENE = scene_combat

            if event.key == pygame.K_RIGHT:
                CURRENT_SCENE = scene_menu

    affiche(screen, CURRENT_SCENE)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()