cs = None

b2 = None
b3 = None
m2 = None
b4 = None
m3 = None
b5 = None
b6 = None
b7 = None
m5 = None
b8 = None
WCA1 = None
WCA2 = None
WCA3 = None
WCA4 = None
NCA1 = None
NCA2 = None
NCA3 = None
NCA4 = None
GMWE = None
GMWN = None
GMWH = None
GMWI = None
GMNE = None
GMNN = None
GMNH = None
GMNI = None

def Get_cube_list(value):
    global cs
    cs = value

def MakeCube():
    global cs, b2, b3, m2, b4, m3, b5, b6, b7, m5, b8, WCA1, WCA2, WCA3, WCA4, NCA1, NCA2, NCA3, NCA4, GMWE, GMWN, GMWH, GMWI, GMNE, GMNN, GMNH, GMNI
    b2 = cs.Typeofcube("noImg",4,"2x2","the mini cube")
    b3 = cs.Typeofcube("noImg",5,"3x3","the clasic cube")
    m2 = cs.Typeofcube("noImg",6,"Mexaming 2x2","a easiest none cube rubix cube")
    b4 = cs.Typeofcube("noImg",6,"4x4","the pro cube")
    m3 = cs.Typeofcube("noImg",7,"Mexaming 3x3","a none cube rubix cube")
    b5 = cs.Typeofcube("noImg",8,"5x5","the master cube")
    b6 = cs.Typeofcube("noImg",9,"6x6","the first none oficial cube")
    b7 = cs.Typeofcube("noImg",10,"7x7","The biggest WCA cube")
    m5 = cs.Typeofcube("noImg",11,"Mexaming 5x5","the biggest none cube rubix cube")
    b8 = cs.Typeofcube("noImg",11,"8x8","first non WCA puzzel's")
    WCA1 = cs.dificulty("easy",1,[b2,b3,b4])
    WCA2 = cs.dificulty("normal",2,[b2,b3,b4,b5,m3])
    WCA3 = cs.dificulty("hard",3,[b2,b3,b4,b5,m3,b6,b7])
    NCA1 = cs.dificulty("easy",2,[b2,b3,b4,m2])
    NCA2 = cs.dificulty("normal",3,[b2,b3,b4,m2,b5,m3])
    NCA3 = cs.dificulty("hard",4,[b2,b3,b4,m2,b5,m3,b6,b7,b8])
    GMWE = cs.GameMode(WCA1,3,"noImg",3,"Wca")
    GMWN = cs.GameMode(WCA2,5,"noImg",3,"Wca")
    GMWH = cs.GameMode(WCA3,8,"noImg",3,"Wca")
    GMNE = cs.GameMode(NCA1,3,"noImg",3,"NO Wca")
    GMNN = cs.GameMode(NCA2,6,"noImg",3,"NO Wca")
    GMNH = cs.GameMode(NCA3,9,"noImg",3,"NO Wca")

