


def calc_Mcd(fck,b,d):
    fcd = 0.85*fck/1.5
    Mcd =  0.275*fcd*b*d*d
    return Mcd

def As(Med, fyk, z):
    fyd = fyk/1.25
    As = Med/(fyd*z)
    return As

def x():
    pass