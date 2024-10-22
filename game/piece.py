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

    def is_enemy_or_empty(self, position, board):
        """Verifica si la posición está vacía o contiene una pieza enemiga."""
        row, col = position
        if 0 <= row < 8 and 0 <= col < 8:  # Verifica los límites del tablero
            piece = board.get_piece(row, col)
            if piece is None or self.is_opponent_piece(piece):
                return True
        return False
