import beamFormulas as b

class Rect_beam:
    def __init__(self, h, b, c) -> None:
        self.h = h
        self.b = b
        self.c = c

class Case1:
    """
    if given rectangular cross and reinforcment
    What is Mrd
    """
    def __init__(self, h, b, As) -> None:
        self.h = h
        self.b = b
        self.As = As

        
