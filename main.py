import pygame
pygame.init()

from affichage import *
from personnage import *
# from time import sleep
from random import randint


scene_combat, scene_menu  = init_scene()

# On ajoute des personnages à la scène de combat
for i in range (5):
    alea = str (randint(0,1)) + str(randint(1,9))
    root = "Images\Personnage\p_" + alea + ".png"
    scene_combat.ajout_elm(Personnage(root))

for i in range(3):
    root = "Images\Personnage\e_01.png"
    scene_combat.ajout_elm(Ennemi(root))


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
            
            if CURRENT_SCENE.nom == "Combat":
                if event.key == pygame.K_DOWN:
                    CURRENT_SCENE.perso[0].vie_baisser(100)


            if event.key == pygame.K_RIGHT:
                CURRENT_SCENE = scene_menu

        
        for bouton in CURRENT_SCENE.file_objets.file:
            if isinstance(bouton, Bouton):

                if bouton.bouton_sous_souris():
                    bouton.couleur_temp = (bouton.couleur[0]+10, bouton.couleur[1]+10, bouton.couleur[2]+10)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        CURRENT_SCENE = scene_combat
                
                else : 
                    bouton.couleur_temp = (bouton.couleur[0]-10, bouton.couleur[1]-10, bouton.couleur[2]-10)

    
    CURRENT_SCENE.affiche(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()