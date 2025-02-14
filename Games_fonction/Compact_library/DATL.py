List_of_type = None
List_of_Dificult = None

cs = None

def Get_Action(value):
    global cs
    cs = value

def Make_Action_List():
    global List_of_type,List_of_Dificult,cs
    List_of_type = [cs.Wca,cs.No_Wca]
    List_of_Dificult = [cs.Easy,cs.Normal,cs.Hard]