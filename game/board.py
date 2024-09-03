from .rook import Rook

class Board:
    def __init__(self):
        # Inicializa el tablero con posiciones vacías
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.__positions__[0][0] = Rook("BLACK")
        self.__positions__[0][7] = Rook("BLACK")
        self.__positions__[7][0] = Rook("WHITE")
        self.__positions__[7][7] = Rook("WHITE")

    def get_piece(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return self.__positions__[row][col]
        else:
            raise IndexError("Position out of board range.")

    def move_piece(self, start_row, start_col, end_row, end_col):
        if 0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8:
            piece = self.__positions__[start_row][start_col]
            self.__positions__[start_row][start_col] = None
            self.__positions__[end_row][end_col] = piece
        else:
            raise IndexError("Move out of board range.")
        
    def is_empty_position(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return self.__positions__[row][col] is None
        else:
            raise IndexError("Position out of board range.")
    
    def place_piece(self, piece, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            self.__positions__[row][col] = piece
        else:
            raise IndexError("Position out of board range.")
