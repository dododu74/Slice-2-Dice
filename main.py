import pygame
from affichage import *

Boite1 = Rectangles('Corps', 10,(175, 96, 26), (80,200,40,200))
Boite2 = Rectangles('Boites Joueurs1', 1, (105, 105, 105), (0, 50, 200, 400))
Boite3 = Rectangles('Boites Joueurs2', 1,(105, 105, 105), (800, 50, 200, 400))
Boite4 = Rectangles('Bras', 10,(175, 96, 26), (30,210,140,20))
Boite0 = Rectangles('Fond', 0,(255, 255, 255), (0,0,1000,500))
Rond1 = Rectangles('Tete', 10,(175, 96, 26), (100, 180), 20)
scene1 = Scene("Combat", (90, 50, 30))
scene1.ajout_elm(Boite0)
scene1.ajout_elm(Boite1)
scene1.ajout_elm(Boite2)
scene1.ajout_elm(Boite3)
scene1.ajout_elm(Boite4)
scene1.ajout_elm(Rond1)

Boite0 = Rectangles('Fond', 0,(150, 100, 255), (0,0,1000,500))
Boite1 = Rectangles('Bouton 1', 100, (175, 96, 26), (400,100, 200,40))
Boite2 = Rectangles('Bouton 2', 19, (175, 96, 26), (440,150, 160,40))
scene2 = Scene("Menu", (100,100,100))
scene2.ajout_elm(Boite0)
scene2.ajout_elm(Boite1)
scene2.ajout_elm(Boite2)






pygame.init()
PLAY = True

pygame.display.set_caption("Slice 2 Dice")
screen = pygame.display.set_mode([1000, 500])


image = pygame.image.load( "Images\Slice_dice.png").convert_alpha()
image = pygame.transform.scale(image, (400, 100))

CURRENT_SCENE = scene2
# Run until the user asks to quit
while PLAY:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PLAY = False
        event.type

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                CURRENT_SCENE = scene1

            if event.key == pygame.K_RIGHT:
                CURRENT_SCENE = scene2    


    print(CURRENT_SCENE.nom)
    affiche(screen, CURRENT_SCENE)

    if CURRENT_SCENE == scene1 :
        screen.blit(image, (300,0))

    # pygame.draw.rect(screen, SCENE.objets["Boite3"].couleur, SCENE.objets["Boite3"].position)
    # pygame.draw.rect(screen, SCENE.objets["Boite2"].couleur, SCENE.objets["Boite2"].position)
    # pygame.draw.rect(screen, SCENE.objets["Boite1"].couleur, SCENE.objets["Boite1"].position)
    # pygame.draw.rect(screen, SCENE.objets["Boite4"].couleur, SCENE.objets["Boite4"].position)
    # pygame.draw.circle(screen, SCENE.objets["Rond1"].couleur, SCENE.objets["Rond1"].position, SCENE.objets["Rond1"].radius)


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()