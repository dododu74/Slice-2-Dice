import pygame
from personnage import *
from TAD import *

if __name__ == '__main__':
    pygame.init()

base_police = pygame.font.Font("Data/JoganSoft.otf",40)

def init_scene():

    # Scene de Combat
    Boite0 = Image('Fond', 0, (0,0),(1000,500), "Images\Background\Cloudy_Mountains.png")

    Boite1 = Rectangles('Boites Joueurs1', 1, (105, 105, 105, 125), (0, 50, 300, 400))    # On définis un rectangle 
    Boite1A = Trans_Rectangles(Boite1, 200)                                               # Et on lui rajoute sa valeure Alpha, de transparence.

    Boite2 = Rectangles('Boites Joueurs2', 1,(105, 105, 105), (700, 50, 300, 400))
    Boite2A = Trans_Rectangles(Boite2, 200)
    
    scene1 = Scene("Combat")
    scene1.ajout_elm(Boite0)
    scene1.ajout_elm(Boite1A)
    scene1.ajout_elm(Boite2A)
    # Exemple de cercles
    # Rond1 = Cercle('Tete', 10,(175, 96, 26), (100, 180), 20)
    # scene1.ajout_elm(Rond1)

    # Scene de Menu
    scene2 = Scene("Menu")
    
    
    Boite1 = Rectangles('Bouton 1', 20, (72, 74, 79), (420,220, 160,50))
    Bouton1 = Bouton("Jouer", Boite1)
    scene2.ajout_elm(Bouton1)
    
    Boite2 = Rectangles('Bouton 2', 20, (175, 96, 0), (400,300, 200,40))
    scene2.ajout_elm(Boite2)

    Image0 = Image('Fond',0, (0,0), (1000,500), "Images/Background/Menu.png")
    scene2.ajout_elm(Image0)

    return scene1 , scene2 


class Rectangles :
    def __init__(self, nom:str, priorit:int, color:tuple, pos:tuple) -> None:
        self.nom = nom
        self.priorite = priorit
        self.couleur = color
        self.position = pos

class Trans_Rectangles : 
    def __init__(self, rectangle:Rectangles, alpha_lv):
        self.Rectangle = rectangle
        self.alpha_lv = alpha_lv
        self.priorite = rectangle.priorite

class Bouton :
    def __init__(self, text, rectangle:Rectangles):
        self.Rectangle = pygame.Rect(rectangle.position)
        self.priorite = rectangle.priorite
        self.couleur = rectangle.couleur
        self.nom = rectangle.nom

        # Initialisation du texte
        self.text_surface = base_police.render(text,False,"black")
        self.text_rectangle = self.text_surface.get_rect(center = self.Rectangle.center)

            
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
        # On ajoute les variable qui vont gérer les joueurs et ennemis en jeux.
        self.perso = []
        self.perso_compteur = 0
        self.ennemi = []
        self.ennemi_compteur = 0

    def ajout_elm(self, elm) :
        # On ajoute un personnage a la scène.
        if  isinstance(elm, Personnage):
            self.perso_compteur += 1
            self.perso.append((elm,self.perso_compteur))

        elif  isinstance(elm, Ennemi):
            self.ennemi_compteur += 1
            self.ennemi.append((elm,self.ennemi_compteur))

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

        
        



def affiche(screen, Scene_to_print:Scene) -> None :
    #on va empecher les effets de bords
    File_objets = Scene_to_print.file_objets.copy()


    # On défile la file d'affichage, et on affiche les éléments selon leurs types
    while not File_objets.file_est_vide():
        elm = File_objets.defiler()   
        
        if isinstance(elm, Rectangles)  :           # Sans transparence
            pygame.draw.rect(screen, elm.couleur, elm.position)

        elif isinstance(elm, Trans_Rectangles) :    # Avec transparence
            positions = elm.Rectangle.position[:]
            s = pygame.Surface(positions[2:])   # On entre les valeures de la position
            s.set_alpha(elm.alpha_lv)           # La valeur alpha
            s.fill(elm.Rectangle.couleur)       # Ensuite on lui met ça couleur
            screen.blit(s, positions[:2])       # Et on la pose à des coordonnées sur l'écran

        elif isinstance(elm, Bouton):
            pygame.draw.rect(screen, elm.couleur, elm.Rectangle)
            screen.blit(elm.text_surface, elm.text_rectangle)

        elif isinstance(elm, Cercle) :
            pygame.draw.circle(screen, elm.couleur, elm.position, elm.radius)

        elif isinstance(elm, Image) :
            image = pygame.image.load( elm.root ).convert_alpha()
            image = pygame.transform.scale(image, elm.format)
            screen.blit(image, elm.position)

    # On affiche maintenant les personnages
    for i in range(len(Scene_to_print.perso)):

        affiche_perso(screen, Scene_to_print.perso[i][0], Scene_to_print.perso[i][1])

    # Et les ennemis 
    for i in range(len(Scene_to_print.ennemi)):

        affiche_ennemi(screen, Scene_to_print.ennemi[i][0], Scene_to_print.ennemi[i][1])
        

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
    # On ajoute des éléments visuels si le personnage est mort
    if not perso.en_vie:
        pygame.draw.polygon(screen, (100,0,0,125), ((pos_x, pos_y), (pos_x + longeur, pos_y + largeur), (pos_x + longeur, pos_y), (pos_x, pos_y + largeur)), 5)

def affiche_ennemi(screen, perso:Ennemi, emplacement):
    pos_x = 720
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
    # On ajoute des éléments visuels si le personnage est mort
    if not perso.en_vie:
        pygame.draw.polygon(screen, (100,0,0,125), ((pos_x, pos_y), (pos_x + longeur, pos_y + largeur), (pos_x + longeur, pos_y), (pos_x, pos_y + largeur)), 5)
