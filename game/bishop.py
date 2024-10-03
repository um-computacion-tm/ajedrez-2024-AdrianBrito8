from .piece import Piece

class Bishop(Piece):
    def __init__(self, color, position=None):
        super().__init__(color)
        self.position = position
    
    def __str__(self):
        if self.get_color() == "WHITE":
            return "B"
        else:
            return "b"
    
    
    def valid_moves(self, position, board=None):
        row, col = position
        moves = []
        # Diagonal moves in all four directions
        for i in range(1, 8):
            if row - i >= 0 and col + i < 8:
                moves.append((row - i, col + i))
            if row - i >= 0 and col - i >= 0:
                moves.append((row - i, col - i))
            if row + i < 8 and col + i < 8:
                moves.append((row + i, col + i))
            if row + i < 8 and col - i >= 0:
                moves.append((row + i, col - i))
        return moves

    
    def can_attack(self, target_position, board):
        if self.position is None:
            raise ValueError("Position of Bishop is not set")
    
        moves = self.valid_moves(self.position)
        return target_position in moves and board.is_enemy_piece(self, target_position)

