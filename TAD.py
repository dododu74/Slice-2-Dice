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
    
    def file_est_vide(self):
        '''Vérifie si la file est vide'''
        return self.file == []

    def enfiler(self, element):
        '''On enfile un élément dans la file'''
        self.file = [element] + self.file

    def defiler(self):
        '''On va défiler un élément dans la file'''
        elm = self.file[-1]
        self.file = self.file[:-1]
        return elm

    def tete(self):
        '''On montre la tête de la file'''
        return self.file[-1]


class Pile:
    def __init__(self):
        '''Crée une pile vide'''
        self.pile = []
    
    def __str__(self):
        reponce = " ︺  "
        for elt in self.pile:
            if len(str(elt)) > 1 :
                reponce = f"┃{elt}┃\n" + reponce
            else : 
                reponce = f"┃ {elt}┃\n" + reponce
        return reponce
    
    def pile_est_vide(self):
        '''Vérifie si la pile est vide'''
        return self.pile == []

    def empiler(self, element):
        '''On enpile un élément dans la pile'''
        self.pile = self.pile + [element]

    def depiler(self):
        '''On va dépiler un élément dans la pile et return la valeurs retiré'''
        sommet = self.pile[-1]
        self.pile = self.pile[:-1]
        return sommet

    def sommet(self):
        '''On montre la sommet de la pile'''
        return self.pile[-1]

    def taille(self):
        return len(self.pile)