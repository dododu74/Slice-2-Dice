import pygame
from TAD import *

class Rectangles :
    def __init__(self, valeur, priorite, color, pos, radius = None) -> None:
        self.valeur = valeur
        self.priorite = priorite
        self.couleur = color
        self.position = pos
        self.radius = radius

class Scene :
    def __init__(self, nom, couleur_de_fond = (255,255,255)) -> None:
        self.nom = nom
        self.couleur_fond = couleur_de_fond
        self.pile_objets = Pile()

    def ajout_elm(self, elm :Rectangles) :
        self.pile_objets.empiler(elm)
    
    def trier_objets(self):
        liste = []
        liste_priorite = []
        for i in range(self.pile_objets.taille()):
            elm = self.pile_objets.depiler
            liste.append(elm)
            liste_priorite.append(elm.priorite)
        sorted(liste_priorite)

        print(liste_priorite,liste)

        
        



def affiche(screen, Scene_to_print:Scene):
    Scene_to_print.trier_objets()
    while not Scene_to_print.pile_objets.pile_est_vide():
        elm = Scene_to_print.pile_objets.depiler()   
             
        if elm.radius == None :
            pygame.draw.rect(screen, elm.couleur, elm.position)
        else :
            pygame.draw.circle(screen, elm.couleur, elm.position, elm.radius)