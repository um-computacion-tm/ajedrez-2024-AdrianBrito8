from .piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        return f"R({self.__color__[0]})"