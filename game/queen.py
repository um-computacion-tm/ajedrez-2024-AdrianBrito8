from .piece import Piece
from .rook import Rook
from .bishop import Bishop

class Queen(Piece):
    def __init__(self, color, position=None):
        super().__init__(color)
        self.rook = Rook(color)
        self.bishop = Bishop(color)
        self.position = position

    def __str__(self):
        return "Q" if self.get_color() == "WHITE" else "q"
    
    def set_position(self, position):
        self.position = position

    def valid_moves(self, position, board=None):
        rook_moves = self.rook.valid_moves(position)
        bishop_moves = self.bishop.valid_moves(position)
        return rook_moves + bishop_moves

    def can_attack(self, target_position, board):
        moves = self.valid_moves(self.position)
        return target_position in moves and board.is_enemy_piece(self, target_position)

    def move(self, new_position, board):

        if new_position in self.valid_moves(self.position, board):
            start_row, start_col = self.position
            end_row, end_col = new_position
            board.move_piece(start_row, start_col, end_row, end_col)  # Pasar filas y columnas
            self.set_position(new_position)
            return True
        return False
