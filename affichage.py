import pygame
from TAD import *


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
    def __init__(self, nom, couleur_de_fond = (255,255,255)) -> None:
        self.nom = nom
        self.couleur_fond = couleur_de_fond
        self.file_objets = File()

    def ajout_elm(self, elm) :
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
    #on va empeicher les effets de bords
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

            