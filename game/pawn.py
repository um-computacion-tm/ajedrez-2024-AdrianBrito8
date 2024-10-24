from .piece import Piece
from .queen import Queen
from .rook import Rook
from .bishop import Bishop
from .knight import Knight

class Pawn(Piece):
    def __init__(self, color, position=None):
        super().__init__(color)
        self.__moved__ = False  
        self.position = position
    
    def __str__(self):
        if self.get_color() == "WHITE":
            return "P"
        else:
            return "p"

    def valid_moves(self, position, board=None):
        row, col = position
        moves = []

        # Determine the direction based on the Pawn's color
        direction = -1 if self.get_color() == "WHITE" else 1

        # Forward move
        forward_move = (row + direction, col)
        if 0 <= forward_move[0] < 8 and board.is_empty_position(*forward_move):
            moves.append(forward_move)

        # Double forward move (only from starting position)
        if not self.__moved__:
            double_forward_move = (row + 2 * direction, col)
            if (0 <= double_forward_move[0] < 8 and
                board.is_empty_position(*forward_move) and
                board.is_empty_position(*double_forward_move)):
                moves.append(double_forward_move)

        # Diagonal captures (solo si hay una pieza enemiga)
        for diagonal_col in [col - 1, col + 1]:
            diagonal_move = (row + direction, diagonal_col)
            if (0 <= diagonal_move[0] < 8 and
                0 <= diagonal_move[1] < 8):  # Asegurarse de que la columna está dentro de los límites
                target_piece = board.get_piece(*diagonal_move)
                if target_piece is not None and target_piece.get_color() != self.get_color():
                    moves.append(diagonal_move)

        return moves

    def move(self, new_position):
        self.position = new_position
        self.__moved__ = True

    def can_attack(self, target_position, board):
        """
        Verifica si el peón puede atacar una pieza enemiga en la posición de destino.
        """
        if not self.position:
            raise ValueError("La posición del peón no está definida.")
        
        current_row, current_col = self.position
        target_row, target_col = target_position

        # El peón ataca solo en diagonal un paso
        direction = -1 if self.get_color() == "WHITE" else 1

        # Verificar que el movimiento es un paso en diagonal
        if abs(target_col - current_col) == 1 and target_row - current_row == direction:
            target_piece = board.get_piece(target_row, target_col)
            if target_piece is not None and target_piece.get_color() != self.get_color():
                return True
        
        return False

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
