class Personnage():
    def __init__(self, image_root="Images\Sprites\PropsInPixels_16x60.png"):
        self.en_vie = True
        self.pts_vie = 10
        self.pts_vie_max = 10
        self.image_root = image_root
    
    def set_vie_max(self, vie):
        self.pts_vie_max = vie
        self.pts_vie = vie

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
        self.image_root = "Images\Sprites\PropsInPixels_16x70.png"

class Ennemi():
    def __init__(self, image_root="Images\Sprites\PropsInPixels_16x70.png"):
        self.en_vie = True
        self.pts_vie = 10
        self.pts_vie_max = 10
        self.image_root = image_root
    
    def set_vie_max(self, vie):
        self.pts_vie_max = vie
        self.pts_vie = vie

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
        self.image_root = "Images\Sprites\PropsInPixels_16x70.png"