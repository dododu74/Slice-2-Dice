import pygame
class Personnage():
    def __init__(self, image_root="Images\Sprites\PropsInPixels_16x60.png", max_hp = 10):
        self.en_vie = True
        self.pts_vie = max_hp
        self.pts_vie_max = max_hp
        self.image_root = image_root
    
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
        self.image_root = "Images\Etat\mort.png"

    def est_en_vie(self):
        return self.en_vie

    def affiche_pts_vie(self, screen, position ):
        
        pos_x , pos_y = position[0] , position[1]
        pos_x += 50
        pos_y += 10 

        for i in range(self.pts_vie):
            image = pygame.image.load("Images\Etat\pts_vie_full.png").convert_alpha()
            image = pygame.transform.scale(image, (20,20))
            screen.blit(image, (pos_x, pos_y))
            pos_x += 10
            
            if i == 9 or i == 19 :
                pos_x = position[0] + 50
                pos_y += 10

        
        for j in range(self.pts_vie_max - self.pts_vie) :
            image = pygame.image.load("Images\Etat\pts_vie_empty.png").convert_alpha()
            image = pygame.transform.scale(image, (20,20))
            screen.blit(image, (pos_x, pos_y))
            pos_x += 10

            if i+j == 9 or i+j == 19 :
                pos_x = position[0] + 50
                pos_y += 10


class Ennemi():
    def __init__(self, image_root="Images\Sprites\PropsInPixels_16x70.png", max_hp = 10):
        self.en_vie = True
        self.pts_vie = max_hp
        self.pts_vie_max = max_hp
        self.image_root = image_root
    
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
        self.image_root = "Images\Etat\mort.png"

    def est_en_vie(self):
        return self.en_vie
    
    def affiche_pts_vie(self, screen, position ):
        pos_x , pos_y = position[0] , position[1]
        pos_x += 50
        pos_y += 10 

        for i in range(self.pts_vie):
            image = pygame.image.load("Images\Etat\pts_vie_full.png").convert_alpha()
            image = pygame.transform.scale(image, (20,20))
            screen.blit(image, (pos_x, pos_y))
            pos_x += 10

            if i == 9 or i == 19 :
                pos_x = position[0] + 50
                pos_y += 10

        for j in range(self.pts_vie_max - self.pts_vie) :
            image = pygame.image.load("Images\Etat\pts_vie_empty.png").convert_alpha()
            image = pygame.transform.scale(image, (20,20))
            screen.blit(image, (pos_x, pos_y))
            pos_x += 10

            if i+j == 9 or i+j == 19 :
                pos_x = position[0] + 50
                pos_y += 10