import pygame
from personnage import *
from TAD import *



def init_scene():
    # Scene de Combat
    Boite0 = Image('Fond', 0, (0,0),(1000,500), "Images\Background\Cloudy_Mountains.png")
    Boite2 = Rectangles('Boites Joueurs1', 1, (105, 105, 105), (0, 50, 300, 400))
    Boite3 = Rectangles('Boites Joueurs2', 1,(105, 105, 105), (700, 50, 300, 400))

    # Rond1 = Cercle('Tete', 10,(175, 96, 26), (100, 180), 20)
    scene1 = Scene("Combat")
    scene1.ajout_elm(Boite0)
    scene1.ajout_elm(Boite2)
    scene1.ajout_elm(Boite3)

    # scene1.ajout_elm(Rond1)

    # Scene de Menu
    Boite1 = Rectangles('Bouton 1', 20, (175, 96, 0), (400,300, 200,40))
    Boite2 = Rectangles('Bouton 2', 20, (0, 96, 26), (420,230, 160,40))
    Image0 = Image('Fond',0, (0,0), (1000,500), "Images/Background/Menu.png")
    scene2 = Scene("Menu")
    # scene2.ajout_elm(Boite0)
    scene2.ajout_elm(Boite1)
    scene2.ajout_elm(Boite2)
    scene2.ajout_elm(Image0)

    return scene1 , scene2 

class Rectangles :
    def __init__(self, nom:str, priorit:int, color:tuple, pos:tuple) -> None:
        self.nom = nom
        self.priorite = priorit
        self.couleur = color
        self.position = pos
    
class Cercle :
    def __init__(self, nom:str, priorit:int, color:tuple, pos:tuple, radius) -> None:
        self.nom = nom
        self.priorite = priorit
        self.couleur = color
        self.position = pos
        self.radius = radius

class Image :
    def __init__(self, nom:str, priorit:int, pos:tuple, format, root) -> None:
        self.nom = nom
        self.priorite = priorit
        self.position = pos
        self.format = format
        self.root = root


class Scene :
    def __init__(self, nom) -> None:
        self.nom = nom
        self.file_objets = File()
        self.perso = []
        self.perso_compteur = 0

    def ajout_elm(self, elm) :
        # On ajoute un personnage a la scène.
        if  isinstance(elm, Personnage):
            self.perso_compteur += 1
            self.perso.append((elm,self.perso_compteur))

        # On ajoute des recanges, ronds ou image a la scène
        else :
            
            if self.file_objets.file_est_vide() :
                self.file_objets.enfiler(elm)
            
            elif elm.priorite < self.file_objets.queue().priorite :
                new_file_objets = File()
                ajoutee = False
                
                while not self.file_objets.file_est_vide() :
                
                    temp = self.file_objets.defiler()
                    if temp.priorite >= elm.priorite and not ajoutee :
                        new_file_objets.enfiler(elm)
                        ajoutee = True
                    new_file_objets.enfiler(temp)
                
                self.file_objets = new_file_objets

            else :
                self.file_objets.enfiler(elm)


    # def trier_objets(self):
    #     liste = []
    #     liste_priorite = []
    #     for i in range(self.pile_objets.taille()):
    #         elm = self.pile_objets.depiler()
    #         liste.append(elm)
    #         liste_priorite.append(elm.priorite)
    #     sorted(liste_priorite)

    #     print(liste_priorite,liste)

        
        



def affiche(screen, Scene_to_print:Scene):
    #on va empecher les effets de bords
    File_objets = Scene_to_print.file_objets.copy()

    #screen.fill(Scene_to_print.couleur_fond)
    while not File_objets.file_est_vide():
        elm = File_objets.defiler()   
        
        if isinstance(elm, Rectangles)  :
            pygame.draw.rect(screen, elm.couleur, elm.position)
        elif isinstance(elm, Cercle) :
            pygame.draw.circle(screen, elm.couleur, elm.position, elm.radius)
        elif isinstance(elm, Image) :
            image = pygame.image.load( elm.root ).convert_alpha()
            image = pygame.transform.scale(image, elm.format)
            screen.blit(image, elm.position)
    
    # On affiche maintenant les personnages
    for i in range(len(Scene_to_print.perso)):

        affiche_perso(screen, Scene_to_print.perso[i][0], Scene_to_print.perso[i][1])

        

def affiche_perso(screen, perso:Personnage, emplacement):
    pos_x = 20
    pos_y = 75 * emplacement 
    longeur = 250
    largeur = 50
    # On affiche le cadre dédié au personnage
    pygame.draw.rect(screen, (150,150,150), (pos_x, pos_y, longeur, largeur), 0  ,  15)
    pygame.draw.rect(screen, (0,0,0), (pos_x, pos_y, longeur, largeur), 5  ,  15)
    # On affiche l'image du personnage
    image = pygame.image.load(perso.image_root).convert_alpha()
    image = pygame.transform.scale(image, (40, 40))
    screen.blit(image, (pos_x + 5, pos_y + 5))

