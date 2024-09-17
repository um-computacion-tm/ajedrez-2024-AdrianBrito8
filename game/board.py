from game.rook import Rook
from game.queen import Queen
from game.bishop import Bishop
from game.knight import Knight
from game.king import King
from game.pawn import Pawn
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition

class Board:
    def __init__(self):
        # Inicializa el tablero con posiciones vacías
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.setup_initial_pieces()

    def setup_initial_pieces(self):
        # Coloca peones
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK")
            self.__positions__[6][col] = Pawn("WHITE")
    
        # Coloca torres
        self.__positions__[0][0] = Rook("BLACK")
        self.__positions__[0][7] = Rook("BLACK")
        self.__positions__[7][0] = Rook("WHITE")
        self.__positions__[7][7] = Rook("WHITE")

        # Coloca caballos
        self.__positions__[0][1] = Knight("BLACK")
        self.__positions__[0][6] = Knight("BLACK")
        self.__positions__[7][1] = Knight("WHITE")
        self.__positions__[7][6] = Knight("WHITE")

        # Coloca alfiles
        self.__positions__[0][2] = Bishop("BLACK")
        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[7][2] = Bishop("WHITE")
        self.__positions__[7][5] = Bishop("WHITE")

        # Coloca reinas
        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[7][3] = Queen("WHITE")

        # Coloca reyes
        self.__positions__[0][4] = King("BLACK")
        self.__positions__[7][4] = King("WHITE")

    
    def get_piece(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return self.__positions__[row][col]
        else:
            raise IndexError("Position out of board range.")

    def move_piece(self, start_row, start_col, end_row, end_col):
        if 0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8:
            piece = self.__positions__[start_row][start_col]
            if piece is None:
                raise EmptyPosition("No piece at the source position.")
            if not self.is_empty_position(end_row, end_col) and self.is_enemy_piece(piece, (end_row, end_col)):
                raise InvalidMove("Cannot move to a position occupied by an enemy piece.")
        
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
        
    def is_enemy_piece(self, piece, position):
        row, col = position
        target_piece = self.get_piece(row, col)
        return target_piece is not None and target_piece.get_color() != piece.get_color()
    
    def set_piece(self, position, piece):
        row, col = position
        self.__positions__[row][col] = piece
