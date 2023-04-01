import pygame



class Rectangles :
    def __init__(self, valeur, color, pos, radius = None) -> None:
        self.valeur = valeur
        self.couleur = color
        self.position = pos
        self.radius = radius

class Scene :
    def __init__(self, nom, couleur_de_fond = (255,255,255)) -> None:
        self.nom = nom
        self.couleur_fond = couleur_de_fond
        self.objets = {}

    def ajout_elm(self, elm :Rectangles) :
        self.objets[elm.valeur] = elm



Boite1 = Rectangles('Boite1', (175, 96, 26), (80,200,40,200))
Boite2 = Rectangles('Boite2', (105, 105, 105), (0, 50, 200, 400))
Boite3 = Rectangles('Boite3', (105, 105, 105), (800, 50, 200, 400))
Boite4 = Rectangles('Boite4', (175, 96, 26), (30,210,140,20))
Rond1 = Rectangles('Rond1', (175, 96, 26), (100, 180), 20)
SCENE = Scene("Combat", (90, 50, 30))
SCENE.ajout_elm(Boite1)
SCENE.ajout_elm(Boite2)
SCENE.ajout_elm(Boite3)
SCENE.ajout_elm(Boite4)
SCENE.ajout_elm(Rond1)



pygame.init()
PLAY = True

pygame.display.set_caption("Slice 2 Dice")
screen = pygame.display.set_mode([1000, 500])

# Fill the background with white
screen.fill(SCENE.couleur_fond)


# Run until the user asks to quit
while PLAY:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            PLAY = False
        event.type


    

    

    pygame.draw.rect(screen, SCENE.objets["Boite3"].couleur, SCENE.objets["Boite3"].position)
    pygame.draw.rect(screen, SCENE.objets["Boite2"].couleur, SCENE.objets["Boite2"].position)
    pygame.draw.rect(screen, SCENE.objets["Boite1"].couleur, SCENE.objets["Boite1"].position)
    pygame.draw.rect(screen, SCENE.objets["Boite4"].couleur, SCENE.objets["Boite4"].position)
    pygame.draw.circle(screen, SCENE.objets["Rond1"].couleur, SCENE.objets["Rond1"].position, SCENE.objets["Rond1"].radius)


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()