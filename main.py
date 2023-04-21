import pygame
pygame.init()

from affichage import *
from personnage import *
# from time import sleep



PLAY = True
pygame.display.set_caption("Slice 2 Dice")
screen = pygame.display.set_mode([1000, 500])

CURRENT_SCENE = init_scene_menu()
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
                    CURRENT_SCENE.perso[0].vie_baisser(1)

        
        for bouton in CURRENT_SCENE.file_objets.file:
            if isinstance(bouton, Bouton):

                if bouton.bouton_sous_souris():
                    bouton.couleur_temp = (bouton.couleur[0]+10, bouton.couleur[1]+10, bouton.couleur[2]+10)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        CURRENT_SCENE = init_scene_combat()
                
                else : 
                    bouton.couleur_temp = (bouton.couleur[0]-10, bouton.couleur[1]-10, bouton.couleur[2]-10)

    
    CURRENT_SCENE.affiche(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()