class Piece:
    def __init__(self, color):
        self.__color__ = color

    def get_color(self):
        return self.__color__
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.__color__})"