import pygame
from random import randint

class Atk_epee:
    def __init__(self, pts_atk):
        self.pts_atk = pts_atk
        self.image_root = "Images/Attaque/Epee.png"

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
    def __init__(self, image_root="Images/Sprites/PropsInPixels_16x60.png", max_hp = 10):
        self.en_vie = True
        self.pts_vie = max_hp
        self.pts_vie_max = max_hp
        self.image_root = image_root

        # Attaques du personnage
        self.capacite = Capacite()

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

    def affiche_pts_vie(self, screen, position ):
        pos_x , pos_y = position[0] , position[1]
        pos_x += 50
        pos_y += 10 

        for i in range(self.pts_vie):
            image = pygame.image.load("Images/Etat/pts_vie_full.png").convert_alpha()
            image = pygame.transform.scale(image, (20,20))
            screen.blit(image, (pos_x, pos_y))
            pos_x += 10
            
            if i == 9 or i == 19 :
                pos_x = position[0] + 50
                pos_y += 10

        i = self.pts_vie - 1
        for j in range(self.pts_vie_max - self.pts_vie) :
            image = pygame.image.load("Images/Etat/pts_vie_empty.png").convert_alpha()
            image = pygame.transform.scale(image, (20,20))
            screen.blit(image, (pos_x, pos_y))
            pos_x += 10

            if i+j == 9 or i+j == 19 :
                pos_x = position[0] + 50
                pos_y += 10

    # L'ensemple des fonction relatives aux capacités  
    def set_capacite(self, new_capacite:Capacite) :
        self.capacite = new_capacite
    
    def add_capacite(self, new_capacite) :
        self.capacite.add_cap(new_capacite)
    
    def get_action_alea(self):
        return self.capacite.alea_cap()
    
    def affiche_action(self, screen, action, position ):
        
        if isinstance(action, No_action) :
            image = pygame.image.load(action.image_root).convert_alpha()
            image = pygame.transform.scale(image, (30,30))
            screen.blit(image, position)
        
        if isinstance(action, Atk_epee) :
            image = pygame.image.load(action.image_root).convert_alpha()
            image = pygame.transform.scale(image, (30,30))
            screen.blit(image, position)
        


        # if isinstance(action, Block) :
        #     image = pygame.image.load("Images\Attaque\Epee.png").convert_alpha()
        #     image = pygame.transform.scale(image, (100,100) ) #position[2:]
        #     screen.blit(image, (500,100))


class Ennemi():
    def __init__(self, image_root="Images/Sprites/PropsInPixels_16x70.png", max_hp = 10):
        self.en_vie = True
        self.pts_vie = max_hp
        self.pts_vie_max = max_hp
        self.image_root = image_root

        # Attaques du personnage
        self.capacite = Capacite()

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
    
    def affiche_pts_vie(self, screen, position ):
        pos_x , pos_y = position[0] , position[1]
        pos_x += 50
        pos_y += 10 

        for i in range(self.pts_vie):
            image = pygame.image.load("Images/Etat/pts_vie_full.png").convert_alpha()
            image = pygame.transform.scale(image, (20,20))
            screen.blit(image, (pos_x, pos_y))
            pos_x += 10

            if i == 9 or i == 19 :
                pos_x = position[0] + 50
                pos_y += 10

        i = self.pts_vie - 1
        for j in range(self.pts_vie_max - self.pts_vie) :
            image = pygame.image.load("Images/Etat/pts_vie_empty.png").convert_alpha()
            image = pygame.transform.scale(image, (20,20))
            screen.blit(image, (pos_x, pos_y))
            pos_x += 10

            if i+j == 9 or i+j == 19 :
                pos_x = position[0] + 50
                pos_y += 10

    # L'ensemple des fonction relatives aux capacités  
    def set_capacite(self, new_capacite:Capacite) :
        self.capacite = new_capacite
    
    def add_capacite(self, new_capacite) :
        self.capacite.add_cap(new_capacite)
    
    def get_action_alea(self):
        return self.capacite.alea_cap()
    
    def affiche_action(self, screen, action, position ):
        
        if isinstance(action, No_action) :
            image = pygame.image.load(action.image_root).convert_alpha()
            image = pygame.transform.scale(image, (30,30))
            screen.blit(image, position)
        
        if isinstance(action, Atk_epee) :
            image = pygame.image.load(action.image_root).convert_alpha()
            image = pygame.transform.scale(image, (30,30))
            screen.blit(image, position)

