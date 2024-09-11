from .piece import Piece
from .board import Board
from .queen import Queen
from .rook import Rook
from .bishop import Bishop
from .knight import Knight

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__moved__ = False  

    def valid_moves(self, position, board=None):
        row, col = position
        moves = []

        if self.get_color() == "WHITE":
            direction = -1  # Peón blanco se mueve hacia arriba
            promotion_row = 0
        else:
            direction = 1  # Peón negro se mueve hacia abajo
            promotion_row = 7

        # Movimiento hacia adelante
        forward_move = (row + direction, col)
        if 0 <= forward_move[0] < 8 and board.is_empty_position(*forward_move):
            moves.append(forward_move)

        # Movimiento doble hacia adelante si no ha movido
        if not self.__moved__:
            double_forward_move = (row + 2 * direction, col)
            if 0 <= double_forward_move[0] < 8 and board.is_empty_position(*double_forward_move):
                moves.append(double_forward_move)

        # Captura en diagonal
        for diagonal_col in [col - 1, col + 1]:
            diagonal_move = (row + direction, diagonal_col)
            if 0 <= diagonal_move[0] < 8 and 0 <= diagonal_move[1] < 8:
                piece = board.get_piece(*diagonal_move)
                if piece is not None and piece.get_color() != self.get_color():
                    moves.append(diagonal_move)

        return moves

    def move(self):
        self.__moved__ = True

    def promote(self, choice):
        """Promociona el peón a la pieza elegida por el jugador."""
        if choice == "queen":
            return Queen(self.get_color())
        elif choice == "rook":
            return Rook(self.get_color())
        elif choice == "bishop":
            return Bishop(self.get_color())
        elif choice == "knight":
            return Knight(self.get_color())
        else:
            raise ValueError("Promoción inválida")
