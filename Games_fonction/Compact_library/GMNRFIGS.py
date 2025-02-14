def GMNRFI(n1,n2):
    a = n1 > n2 and n1 < n2+2
    b = n1 < n2 and n1 > n2-2
    return a or b