class Type:
    def __init__(self,Carater,name):
        self.Carater = Carater
        self.name = name

class Dificulty:
    def __init__(self,Carater,name):
        self.Carater = Carater
        self.name = name

Wca = Type("W","Wca")
No_Wca = Type("N","No Wca")
Easy = Dificulty("E","Easy")
Normal = Dificulty("N","Normal")
Hard = Dificulty("H","Hard")

def Build_dificulty(type:Type,Dificulty:Dificulty):
    return "GM" + type.Carater + Dificulty.Carater

print(Build_dificulty(Wca,Hard))