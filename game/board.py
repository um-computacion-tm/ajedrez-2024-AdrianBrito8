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
        self.current_turn = "WHITE"

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
        if not self._in_bounds(start_row, start_col) or not self._in_bounds(end_row, end_col):
            raise IndexError("Move out of board range.")

        piece = self.__positions__[start_row][start_col]
        if piece is None:
            raise EmptyPosition("No piece at the source position.")

        # Verificar si es el turno correcto
        if piece.get_color() != self.current_turn:
            raise InvalidTurn("It's not your turn.")

        # Verificar si el movimiento es válido para la pieza
        valid_moves = piece.valid_moves((start_row, start_col), self)
        if (end_row, end_col) not in valid_moves:
            raise InvalidMove("Invalid move for the piece.")

        # Realizar el movimiento
        self.__positions__[start_row][start_col] = None
        self.__positions__[end_row][end_col] = piece

        # Cambiar el turno
        self.current_turn = "WHITE" if self.current_turn == "BLACK" else "BLACK"

    def is_empty_position(self, row, col):
        if self._in_bounds(row, col):
            return self.__positions__[row][col] is None
        else:
            raise IndexError("Position out of board range.")
    
        
    def is_enemy_piece(self, piece, position):
        row, col = position
        target_piece = self.get_piece(row, col)
        return target_piece is not None and target_piece.get_color() != piece.get_color()
    
    
    def _in_bounds(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def update_position(self, position, piece=None):
        """
        Actualiza la posición en el tablero, ya sea para colocar o remover una pieza.
        Si `piece` es `None`, se considera que se está removiendo la pieza.
        """
        row, col = position
        if self._in_bounds(row, col):
            self.__positions__[row][col] = piece
        else:
            raise IndexError("Position out of board range.")

    def place_piece(self, piece, row, col):
        self.update_position((row, col), piece)

    def set_piece(self, position, piece):
        self.update_position(position, piece)

    def remove_piece(self, row, col):
        self.update_position((row, col), None)


    def show_board(self):
        board_str = ""
        for row in range(8):
            board_str += str(8 - row) + " "  # Mostrar números de fila de 8 a 1
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece is None:
                    board_str += ". "  # Casilla vacía
                else:
                    if piece.get_color() == "WHITE":
                        board_str += str(piece).upper() + " "
                    else:
                        board_str += str(piece).lower() + " "

            board_str += "\n"
            
        board_str += "  a b c d e f g h\n"  # Mostrar letras de columna de 'a' a 'h'
        return board_str
    
    def get_king_position(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece is not None and isinstance(piece, King) and piece.get_color() == color:
                    return (row, col)

        return None