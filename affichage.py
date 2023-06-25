import pygame
from personnage import *
from TAD import *
from random import randint

if __name__ == '__main__':
    pygame.init()

base_police = pygame.font.Font( "Data/JoganSoft.otf" ,40)

def init_scene_menu():
    # Scene de Menu
    scene = Scene("Menu")

    Boite1 = Rectangles('Bouton 1', 20, (72, 74, 79), (420,220, 160,50))
    code1= """
from affichage import init_scene_combat
CURRENT_SCENE = init_scene_combat()
"""
    Bouton1 = Bouton("Jouer", Boite1, code1)
    
    scene.ajout_elm(Bouton1)

    Boite2 = Rectangles('Bouton 2', 20, (175, 96, 0), (400,300, 200,40))
    scene.ajout_elm(Boite2)

    Image0 = Image('Fond',0, (0,0), (1000,500), "Images/Background/Menu.png")
    scene.ajout_elm(Image0)

    return scene 

def init_scene_combat():
    # Scene de Combat
    Boite0 = Image('Fond', 0, (0,0),(1000,500), "Images/Background/Cloudy_Mountains.png")

    Boite1 = Rectangles('Boites Joueurs1', 1, (105, 105, 105, 125), (0, 50, 300, 400))    # On définis un rectangle 
    Boite1A = Trans_Rectangles(Boite1, 200)                                               # Et on lui rajoute sa valeure Alpha, de transparence.

    Boite2 = Rectangles('Boites Joueurs2', 1,(105, 105, 105), (700, 50, 300, 400))
    Boite2A = Trans_Rectangles(Boite2, 200)
    
    scene = Scene("Combat")
    scene.ajout_elm(Boite0)
    scene.ajout_elm(Boite1A)
    scene.ajout_elm(Boite2A)

    Boite3 = Rectangles('Bouton 1', 20, (72, 74, 79), (400,420, 200,50))
    code3 = """
CURRENT_SCENE.etat += 1
"""
    Bouton3 = Bouton("Passer", Boite3, code3)
    scene.ajout_elm(Bouton3)

    # Exemple de cercles
    # Rond1 = Cercle('Tete', 10,(175, 96, 26), (100, 180), 20)
    # scene1.ajout_elm(Rond1)

    
    # On ajoute des personnages à la scène
    for i in range(5):
        alea = str (randint(0,1)) + str(randint(1,8))
        personnage = Personnage( i , "Images/Personnage/p_" + alea + ".png", 35)
        
        scene.ajout_elm(personnage)

    # On ajoute des ennemis à la scène
    for i in range(2):
        root = "Images/Personnage/e_01.png"
        scene.ajout_elm(Ennemi(i,root, randint(1,290)))
    
    root = "Images/Personnage/e_01.png"
    Bernard = Ennemi(2,root, randint(1,29))
    Bernard.set_capacite(Capacite([No_action(), Atk_epee(1)]))
    scene.ajout_elm(Bernard)

    return scene

class Bouton :
    def __init__(self, text, rectangle:Rectangles, code_to_execute:str):
        self.Rectangle = pygame.Rect(rectangle.position)
        self.priorite = rectangle.priorite
        self.couleur = rectangle.couleur
        self.couleur_temp = rectangle.couleur
        self.nom = rectangle.nom
        self.code = code_to_execute

        # Initialisation du texte
        self.text_surface = base_police.render(text,False,"black")
        self.text_rectangle = self.text_surface.get_rect(center = self.Rectangle.center)
    
    def bouton_sous_souris(self):
        souris_pos = pygame.mouse.get_pos()
        if self.Rectangle.collidepoint(souris_pos) :
            return True

    def executer(self,CURRENT_SCENE):

        # La fonction nécessite un dictionnaire de sortie pour les variables
        variables = {"CURRENT_SCENE":CURRENT_SCENE}

        # Execution du code de type STR du bouton
        exec(self.code, variables)

        # On prend en compte les changements du bouton
        return variables["CURRENT_SCENE"]

class Scene :
    def __init__(self, nom) -> None:
        self.nom = nom
        self.file_objets = File()

        # On ajoute les variable qui vont gérer les joueurs et ennemis en jeux.
        self.perso = []
        self.ennemi = []
        # Ainsi que les tours de jeu
        self.etat = 0

    def ajout_elm(self, elm) :
        # On ajoute un personnage a la scène.
        if  isinstance(elm, Personnage):
            self.perso.append(elm)

        elif  isinstance(elm, Ennemi):
            self.ennemi.append(elm)

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
        
    def affiche(self, screen) -> None :
        #on va empecher les effets de bords
        File_objets = self.file_objets.copy()


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
                pygame.draw.rect(screen, elm.couleur_temp, elm.Rectangle)
                screen.blit(elm.text_surface, elm.text_rectangle)

            elif isinstance(elm, Cercle) :
                pygame.draw.circle(screen, elm.couleur, elm.position, elm.radius)

            elif isinstance(elm, Image) :
                image = pygame.image.load( elm.root ).convert_alpha()
                image = pygame.transform.scale(image, elm.format)
                screen.blit(image, elm.position)
            
            elif isinstance(elm, Ligne) :
                pygame.draw.line(screen, elm.couleur, elm.pointA, elm.pointB, elm.epaisseur)

        # On affiche maintenant les personnages
        for perso in self.perso:
            perso.affiche_perso(screen)

        # Et les ennemis 
        for ennemi in self.ennemi:
            ennemi.affiche_ennemi(screen)


    def tour(self, screen, CURRENT_SCENE) -> None :
        if self.etat ==  0 :

            # On attribut une nouvelle action aux personnages
            for perso in self.perso:
                perso.nouvelle_action()

            for ennemi in self.ennemi:
                ennemi.nouvelle_action()
                ennemi.reset_action_cible()

                # On donne à l'ennemi une cible 
                ennemi.trouver_cible_action()
                # Cible qui doit nécessairement êrte en vie
                while not CURRENT_SCENE.perso[ennemi.action_cible].est_en_vie :
                    ennemi.trouver_cible_action()

                # On met alors en suspen les poinst de vie des personnages
                cible = ennemi.get_cible()
                degats = ennemi.get_action_degats() 
                self.perso[cible].suspendre_vie_add(degats)
            
            # On passe ensuite au tour suivant
            self.etat = 1
        
        elif self.etat == 1 :

            # Pour tous les ennemis
            for ennemi in self.ennemi :
                
                # On affiche ensuite l'action
                ennemi.affiche_action(screen)

            
            # Pour tous les personnages encore vivants
            for perso in self.perso :

                # On affiche en suite l'action
                perso.affiche_action(screen)
                  

        
        elif self.etat == 2 :
            
            for perso in self.perso:
                perso.vie_baisser(perso.pts_vie_suspen)
                perso.pts_vie_suspen = 0


            
            
            
            self.etat = 3
            

        else :
            self.etat = 0

        
        

