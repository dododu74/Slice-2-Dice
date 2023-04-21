class Atk_epee:
    def __init__(self, pts_atk):
        self.pts_atk = pts_atk
        self.image_root = "Images\Attaque\Epee.png"

class Capacite :
    def __init__(self, dict:dict = {}):
        
        for i in range(1,9):

            if str(i) not in dict :
                dict[str(i)] = None
        
        # On a : cap{ligne}{colone}
        self.cap01 = dict["1"]
        self.cap02 = dict["2"]
        self.cap03 = dict["3"]
        self.cap04 = dict["4"]
        self.cap11 = dict["5"]
        self.cap12 = dict["6"]
        self.cap13 = dict["7"]
        self.cap14 = dict["8"]
    
    def get_cap(self, emplacement : tuple):
        
        return self.cap + emplacement[0] + emplacement[1] 

