from .rook import Rook
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition

class Board:
    def __init__(self):
        # Inicializa el tablero con posiciones vacías
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.setup_initial_pieces()

    def setup_initial_pieces(self):
        # Configuración inicial de las piezas
        for col in range(8):
            self.__positions__[1][col] = Rook("BLACK")  # Suponiendo que colocas torres negras en la fila 1
            self.__positions__[6][col] = Rook("WHITE")  # Suponiendo que colocas torres blancas en la fila 6
        
        pieces = [Rook] * 8  # Por ahora, solo rooks como ejemplo; ajusta según sea necesario
        for col, piece_class in enumerate(pieces):
            self.__positions__[0][col] = piece_class("BLACK")
            self.__positions__[7][col] = piece_class("WHITE")
    
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
