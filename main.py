import pygame
from affichage import *
from time import sleep

Boite1 = Rectangles('Corps', 10,(175, 96, 26), (80,200,40,200))
Boite2 = Rectangles('Boites Joueurs1', 1, (105, 105, 105), (0, 50, 200, 400))
Boite3 = Rectangles('Boites Joueurs2', 1,(105, 105, 105), (800, 50, 200, 400))
Boite4 = Rectangles('Bras', 10,(175, 96, 26), (30,210,140,20))
Boite0 = Rectangles('Fond', 0,(255, 255, 255), (0,0,1000,500))
Rond1 = Cercle('Tete', 10,(175, 96, 26), (100, 180), 20)
scene1 = Scene("Combat", (90, 50, 30))
scene1.ajout_elm(Boite0)
scene1.ajout_elm(Boite1)
scene1.ajout_elm(Boite2)
scene1.ajout_elm(Boite3)
scene1.ajout_elm(Boite4)
scene1.ajout_elm(Rond1)

# Boite0 = Rectangles('Fond', 0,(150, 100, 255), (0,0,1000,500))
Boite1 = Rectangles('Bouton 1', 20, (175, 96, 0), (400,300, 200,40))
Boite2 = Rectangles('Bouton 2', 20, (0, 96, 26), (420,230, 160,40))
Image0 = Image('Fond',0, (0,0), (1000,500), "Images/Slice_dice.png")
scene2 = Scene("Menu", (100,100,100))
# scene2.ajout_elm(Boite0)
scene2.ajout_elm(Boite1)
scene2.ajout_elm(Boite2)
scene2.ajout_elm(Image0)






pygame.init()
PLAY = True

pygame.display.set_caption("Slice 2 Dice")
screen = pygame.display.set_mode([1000, 500])



CURRENT_SCENE = scene2
# Run until the user asks to quit
while PLAY:
    # sleep(2)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PLAY = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                CURRENT_SCENE = scene1

            if event.key == pygame.K_RIGHT:
                CURRENT_SCENE = scene2    


    affiche(screen, CURRENT_SCENE)




    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()