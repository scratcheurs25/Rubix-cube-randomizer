def Chose_type(Type_list):
    i = 0
    for e in Type_list:
        i += 1
        print(str(i)+":"+e.name)
    a = input("Which (use the number of it)")
    return Type_list[int(a)-1]

def Chose_Dificult(Dificult_list):
    i = 0
    for e in Dificult_list:
        i += 1
        print(str(i)+":"+e.name)
    a = input("Which (use the number of it)")
    return Dificult_list[int(a)-1]
    