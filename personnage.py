import pygame
from random import randint

class Atk_epee:
    def __init__(self, pts_atk):
        self.pts_atk = pts_atk
        self.image_root = "Images/Attaque/Epee.png"

class Non_choisi : 
    def __init__(self):
        self.image_root = "Images/Attaque/None.png"

class No_action : 
    def __init__(self):
        self.image_root = "Images/Attaque/None.png"

class Capacite :
    def __init__(self, base_cap:list = [No_action(), No_action(), Atk_epee(5)] ):
        self.capacite = base_cap

    def alea_cap(self) :
        i = randint(0,len(self.capacite)-1)
        
        return self.capacite[i]
    
    def add_cap(self, add) :
        self.capacite.append(add)
    
        

class Personnage:
    def __init__(self, emplacement, image_root="Images/Personnage/p_01.png", max_hp = 10):
        self.en_vie = True
        self.pts_vie = max_hp
        self.pts_vie_max = max_hp
        self.image_root = image_root

        # On a ici les coordonnées du personnages, coin supérieur gaughe
        self.emplacement = emplacement
        self.pos = (20, 75 + 75 * emplacement)

        # Attaques du personnage
        self.capacite = Capacite()
        self.action = Non_choisi()

    def set_vie_max(self, vie):
        self.pts_vie_max = vie
        self.pts_vie = vie

    def get_vie(self):
        return self.pts_vie

    def vie_baisser(self, quantite):
        if self.pts_vie > quantite :
            self.pts_vie -= quantite
        else :
            self.mort()
    
    def vie_augmenter(self, quantite):
        if self.pts_vie_max <= quantite :
            self.pts_vie = self.pts_vie_max
        else :
            self.pts_vie += quantite

    def mort(self):
        self.en_vie = False
        self.image_root_avant = self.image_root
        self.image_root = "Images/Etat/mort.png"

    def est_en_vie(self):
        return self.en_vie

    # Les méthodes relatives à l'affichage
    def affiche_perso(self, screen):
        longeur = 250
        largeur = 50
        
        # On affiche le cadre dédié au personnage
        pygame.draw.rect(screen, (150,150,150), (self.pos[0], self.pos[1], longeur, largeur), 0  ,  15)
        pygame.draw.rect(screen, (0,0,0), (self.pos[0], self.pos[1], longeur, largeur), 5  ,  15)
        
        # On affiche l'image du personnage
        image = pygame.image.load(self.image_root).convert_alpha()
        image = pygame.transform.scale(image, (40, 40))
        screen.blit(image, (self.pos[0] + 5, self.pos[1] + 5))

        # On ajoute des éléments visuels si le personnage est mort
        if not self.est_en_vie():
            pygame.draw.polygon(screen, (100,0,0,125), (self.pos, (self.pos[0] + longeur, self.pos[1] + largeur), (self.pos[0] + longeur, self.pos[1]), (self.pos[0], self.pos[1] + largeur )), 5)


        # On affiche les points de vie du personnage sinon
        else :   
            self.affiche_pts_vie(screen)

    def affiche_pts_vie(self, screen):
        
        pos_x = 50 + self.pos[0]
        pos_y = 10 + self.pos[1]

        for i in range(self.pts_vie):
            image = pygame.image.load("Images/Etat/pts_vie_full.png").convert_alpha()
            image = pygame.transform.scale(image, (20,20))
            screen.blit(image, (pos_x, pos_y))
            pos_x += 10
            
            if i == 9 or i == 19 :
                pos_x -= 100
                pos_y += 10

        i = self.pts_vie - 1
        for j in range(self.pts_vie_max - self.pts_vie) :
            image = pygame.image.load("Images/Etat/pts_vie_empty.png").convert_alpha()
            image = pygame.transform.scale(image, (20,20))
            screen.blit(image, (pos_x, pos_y))
            pos_x += 10

            if i+j == 9 or i+j == 19 :
                pos_x -= 100
                pos_y += 10

    # L'ensemple des méthodes relatives aux capacités  
    def set_capacite(self, new_capacite:Capacite) :
        self.capacite = new_capacite

    def nouvelle_action(self):
        self.action = self.capacite.alea_cap()

    def affiche_action(self, screen):
        
        pos_x = self.pos[0] + 190
        pos_y = self.pos[1] + 10

        if isinstance(self.action, No_action) :
            image = pygame.image.load(self.action.image_root).convert_alpha()
            image = pygame.transform.scale(image, (30,30))
            screen.blit(image, (pos_x, pos_y))
        
        if isinstance(self.action, Atk_epee) :
            image = pygame.image.load(self.action.image_root).convert_alpha()
            image = pygame.transform.scale(image, (30,30))
            screen.blit(image, (pos_x, pos_y))


class Ennemi():
    def __init__(self, emplacement:int, image_root="Images/Sprites/PropsInPixels_16x70.png", max_hp = 10):
        self.en_vie = True
        self.pts_vie = max_hp
        self.pts_vie_max = max_hp
        self.image_root = image_root

        # Coordonnées de l'ennemi
        self.emplacement = emplacement
        self.pos = (720, 75 + 75 * emplacement)

        # Attaques de l'ennemi
        self.capacite = Capacite()
        self.action = Non_choisi()

    def set_vie_max(self, vie):
        self.pts_vie_max = vie
        self.pts_vie = vie

    def get_vie(self):
        return self.pts_vie

    def vie_baisser(self, quantite):
        if self.pts_vie > quantite :
            self.pts_vie -= quantite
        else :
            self.mort()
    
    def vie_augmenter(self, quantite):
        if self.pts_vie_max <= quantite :
            self.pts_vie = self.pts_vie_max
        else :
            self.pts_vie += quantite

    def mort(self):
        self.en_vie = False
        self.image_root_avant = self.image_root
        self.image_root = "Images/Etat/mort.png"

    def est_en_vie(self):
        return self.en_vie
    
    # L'ensembles de méthodes d'affichage
    def affiche_ennemi(self, screen):

        longeur = 250
        largeur = 50
        
        # On affiche le cadre dédié au personnage
        pygame.draw.rect(screen, (150,150,150), (self.pos[0], self.pos[1], longeur, largeur), 0  ,  15)
        pygame.draw.rect(screen, (0,0,0), (self.pos[0], self.pos[1], longeur, largeur), 5  ,  15)
        
        # On affiche l'image du personnage
        image = pygame.image.load(self.image_root).convert_alpha()
        image = pygame.transform.scale(image, (40, 40))
        screen.blit(image, (self.pos[0] + 5 , self.pos[1] + 5))

        # On ajoute des éléments visuels si le personnage est mort
        if not self.est_en_vie():
            pygame.draw.polygon(screen, (100,0,0,125), (self.pos, (self.pos[0] + longeur, self.pos[1] + largeur), (self.pos[0] + longeur, self.pos[1]), (self.pos[0], self.pos[1] + largeur )), 5)

        else :

            # On affiche les points de vie du personnage sinon
            self.affiche_pts_vie(screen)
    
    def affiche_pts_vie(self, screen):
        pos_x = 50 + self.pos[0]
        pos_y = 10 + self.pos[1]

        for i in range(self.pts_vie):
            image = pygame.image.load("Images/Etat/pts_vie_full.png").convert_alpha()
            image = pygame.transform.scale(image, (20,20))
            screen.blit(image, (pos_x, pos_y))
            pos_x += 10

            if i == 9 or i == 19 :
                pos_x -= 100
                pos_y += 10

        i = self.pts_vie - 1
        for j in range(self.pts_vie_max - self.pts_vie) :
            image = pygame.image.load("Images/Etat/pts_vie_empty.png").convert_alpha()
            image = pygame.transform.scale(image, (20,20))
            screen.blit(image, (pos_x, pos_y))
            pos_x += 10

            if i+j == 9 or i+j == 19 :
                pos_x -= 100
                pos_y += 10

    # L'ensemple des méthodes relatives aux capacités  
    def set_capacite(self, new_capacite:Capacite) :
        self.capacite = new_capacite
    
    def nouvelle_action(self):
        self.action = self.capacite.alea_cap()

    def affiche_action(self, screen):
        
        pos_x = self.pos[0] + 190
        pos_y = self.pos[1] + 10

        if isinstance(self.action, No_action) :
            image = pygame.image.load(self.action.image_root).convert_alpha()
            image = pygame.transform.scale(image, (30,30))
            screen.blit(image, (pos_x, pos_y))
        
        if isinstance(self.action, Atk_epee) :
            image = pygame.image.load(self.action.image_root).convert_alpha()
            image = pygame.transform.scale(image, (30,30))
            screen.blit(image, (pos_x, pos_y))

    def trouver_cible_action(self, CURRENT_SCENE):
        
        pass
