import random
from Games_fonction.Compact_library.GMNRFIGS import *

class Typeofcube:
    def __init__(self,img,dificulty,name,des):
        self.img = img
        self.dificulty = dificulty
        self.name = name
        self.des = des
class dificulty:
    def __init__(self,name,value,typeofcubes:tuple):
        self.name = name
        self.value = value
        self.typeofcubes = typeofcubes

class GameMode:
    def __init__(self,dificulty:dificulty,long,icon,localdificult,name):
        self.dificulty = dificulty
        self.long = long
        self.life = long
        self.icon = icon
        self.localfificult = localdificult
        self.Blocalfificult = localdificult
        self.name = name
    def ResetLife(self):
        self.life = self.long
    def ResetLocalDificult(self):
        self.localfificult = self.Blocalfificult
    def DecLife(self):
        self.life -= 1
    def IncLocalDificult(self):
        self.localfificult += 1
    def nextRound(self):
        PossibleCube = []
        for e in self.dificulty.typeofcubes:
            if GMNRFI(e.dificulty,self.localfificult):
                PossibleCube.append(e)
        return random.choice(PossibleCube)
        

        