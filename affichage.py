import pygame
from TAD import *

class Rectangles :
    def __init__(self, valeur:str, priorit:int, color:tuple, pos:tuple, radius = None) -> None:
        self.valeur = valeur
        self.priorite = priorit
        self.couleur = color
        self.position = pos
        self.radius = radius

class Scene :
    def __init__(self, nom, couleur_de_fond = (255,255,255)) -> None:
        self.nom = nom
        self.couleur_fond = couleur_de_fond
        self.file_objets = File()

    def ajout_elm(self, elm :Rectangles) :
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
    #screen.fill(Scene_to_print.couleur_fond)
    print(Scene_to_print.file_objets)
    while not Scene_to_print.file_objets.file_est_vide():
        elm = Scene_to_print.file_objets.defiler()   

        if elm.radius == None :
            pygame.draw.rect(screen, elm.couleur, elm.position)
        else :
            pygame.draw.circle(screen, elm.couleur, elm.position, elm.radius)