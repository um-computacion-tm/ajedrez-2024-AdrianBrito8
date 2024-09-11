from .piece import Piece
from .rook import Rook
from .bishop import Bishop

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.rook = Rook(color)
        self.bishop = Bishop(color)
    
    def __str__(self):
        return f"Q({self.get_color()[0]})"
    
    def valid_moves(self, position, board=None):
        rook_moves = self.rook.valid_moves(position)
        bishop_moves = self.bishop.valid_moves(position)
        return rook_moves + bishop_moves

    def can_attack(self, target_position, board):
        """
        Devuelve True si la reina puede atacar la pieza en la posición objetivo.
        """
        moves = self.valid_moves(self.position)
        return target_position in moves and board.is_enemy_piece(self, target_position)
