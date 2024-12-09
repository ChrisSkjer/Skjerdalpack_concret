
def calc_Mcd(fck,b,d):
    """
    Regner ut Mcd for normalarmet tverrsnitt, bruddtøyning stål = 5 promille  
    "normalarmert" x = 0.412*d  
    """
    fcd = 0.85*fck/1.5
    Mcd =  0.275*fcd*b*d*d
    return Mcd

def calc_fyd(fyk):
    alfa = 0.85
    gamma = 1.5
    fyd = alfa*fyk/gamma
    return fyd 

def calc_As(Med, fyk, z):
    fyd = calc_fyd(fyk)
    As = Med/(fyd*z)
    return As

def calc_Msd(fyk, z, As):
    """
    beregner dimensjonerende moment for gitt armering
    må sammenlignes med Mcd
    """
    fyd = calc_fyd(fyk)
    Msd = As/(fyd*z)
    return Msd

def x():
    pass