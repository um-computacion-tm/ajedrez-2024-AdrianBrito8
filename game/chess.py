from game.board import Board
from game.pawn import Pawn
from game.queen import Queen
from game.rook import Rook
from game.bishop import Bishop
from game.knight import Knight
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition

class Chess:
    def __init__(self):
        self.board = Board()
        self.current_turn = "WHITE"  # Comienza con el turno de las piezas blancas

    def move(self, start_row, start_col, end_row, end_col, promotion_choice=None):
        # Verifica el turno actual
        piece = self.board.get_piece(start_row, start_col)
        if piece is None:
            raise EmptyPosition("No piece at the source position.")
        if piece.get_color() != self.current_turn:
            raise InvalidTurn("It is not your turn to move this piece.")
    
        # Verifica el movimiento válido
        if not self.is_valid_move(start_row, start_col, end_row, end_col):
            raise InvalidMove("Invalid move for this piece.")
    
        # Si es un peón y ha llegado al final del tablero, maneja la promoción
        if isinstance(piece, Pawn) and (end_row == 0 or end_row == 7):
            if promotion_choice is None:
                raise ValueError("Promotion choice is required.")
            if promotion_choice not in ["queen", "rook", "bishop", "knight"]:
                raise ValueError("Invalid promotion choice.")
            self.promote_pawn(start_row, start_col, end_row, end_col, promotion_choice)
        else:
            # Mueve la pieza
            self.board.move_piece(start_row, start_col, end_row, end_col)
    
        # Cambia el turno
        self.current_turn = "WHITE" if self.current_turn == "BLACK" else "BLACK"

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        piece = self.board.get_piece(start_row, start_col)
    
        if piece is None:
            return False

        valid_moves = piece.valid_moves((start_row, start_col), self.board)
    
        # Revisar si el movimiento está en la lista de movimientos válidos
        if isinstance(piece, Pawn) and (end_row == 0 or end_row == 7):
            # Allow pawns to move to the opposite side of the board
            return True
        else:
            return (end_row, end_col) in valid_moves

    def promote_pawn(self, start_row, start_col, end_row, end_col, promotion_choice):
        # Implementa la lógica para promover un peón
        color = self.board.get_piece(start_row, start_col).get_color()
        self.board.remove_piece(start_row, start_col)  # Elimina el peón antes de promoverlo

        # Coloca la nueva pieza en la posición de promoción
        if promotion_choice == "queen":
            self.board.place_piece(Queen(color), end_row, end_col)
        elif promotion_choice == "rook":
            self.board.place_piece(Rook(color), end_row, end_col)
        elif promotion_choice == "bishop":
            self.board.place_piece(Bishop(color), end_row, end_col)
        elif promotion_choice == "knight":
            self.board.place_piece(Knight(color), end_row, end_col)
