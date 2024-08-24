class Piece:
    def __init__(self, color):
        self.__color__ = color
        self.__position__ = None
        self.__captured__ = False

    def get_color(self):
        return self.__color__
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.__color__})"
    
    def is_opponent_piece(self, other_piece):
        """Returns True if the other piece is an opponent piece, otherwise False."""
        return self.__color__ != other_piece.get_color()
    
    def set_position(self, position):
        self.__position__ = position

    def get_position(self):
        return self.__position__
    
    def move_to(self, new_position):
        self.__position__ = new_position

    def is_captured(self):
        return self.__captured__

    def capture(self):
        self.__captured__ = True

    def __str__(self):
        return f"{self.__class__.__name__}({self.__color__})"