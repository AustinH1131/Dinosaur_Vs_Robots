from Dinosaur import Dinasaur

class Herd:
    def __innit__(self):
        self.dinasaurs= []
        
    def create_herd(self):
        dino1=Dinasaur("Barney",84,750)
        self.dinasaurs.append(dino1)
        dino2=Dinasaur("Rexy",115,460)
        self.dinasaurs.append(dino2)
        dino3=Dinasaur("Raptor",90,700)
        self.dinasaurs.append(dino3)
herd=Herd()
herd.create_herd()
print(herd.dinasaurs)
