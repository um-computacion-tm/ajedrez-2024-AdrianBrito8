from .piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        return f"R({self.get_color()[0]})"  # Usa get_color() para acceder al color
    
    def valid_moves(self, position):
        row, col = position
        moves = []

        # Horizontal moves
        for c in range(8):
            if c != col:
                moves.append((row, c))
        # Vertical moves
        for r in range(8):
            if r != row:
                moves.append((r, col))
        return moves
    
    def can_attack(self, current_position, other_piece_position):
        row, col = current_position
        valid_moves = self.valid_moves(current_position)
        return other_piece_position in valid_moves
