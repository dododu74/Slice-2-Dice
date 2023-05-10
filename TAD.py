class File:
    def __init__(self):
        '''Crée une file vide'''
        self.file = []
    
    def __str__(self):
        ligne1 = ""
        ligne2 = ""
        for elm in self.file:
            ligne1 += "―"  * (len(str(elm)) + 1 )
            ligne2 += f"{elm} "
        return f"{ligne1}\n{ligne2}\n{ligne1}"
    
    def copy(self):
        new_file = File()
        for i in range (self.taille()-1,-1,-1):
            new_file.enfiler(self.file[i])
        return new_file

    def file_est_vide(self) -> bool:
        '''Vérifie si la file est vide'''
        return self.file == []

    def enfiler(self, element) -> None:
        '''On enfile un élément dans la file'''
        self.file = [element] + self.file

    def defiler(self):
        '''On va défiler un élément dans la file et le retourner'''
        elm = self.file[-1]
        self.file = self.file[:-1]
        return elm

    def tete(self):
        '''On montre la tête de la file'''
        return self.file[-1]

    def queue(self):
        '''On montre quel est le dernier élément a être entré dans la file'''
        return self.file[0]



    def taille(self) -> int:
        '''On return la taille de la file'''
        return len (self.file)
#### L'ensemble des classes qui sont des objets utiles aux Scènes

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

class Ligne :
    def __init__(self, priorit:int, color:tuple, pointA:tuple, pointB:tuple, epaisseur:int ):
        self.priorite = priorit
        self.couleur = color
        self.pointA = pointA
        self.pointB = pointB
        self.epaisseur = epaisseur