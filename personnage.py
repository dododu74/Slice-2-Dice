from random import randint

class Personnage():
    def __init__(self, image_root="Images\Sprites\PropsInPixels_16x60.png"):
        self.pts_vie = 10
        self.pts_vie_max = 10
        self.image_root = "Images\Sprites\PropsInPixels_16x" + str(randint(1,172)) + ".png"