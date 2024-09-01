from .piece import Piece

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        return f"B({self.get_color()[0]})"
    
    def valid_moves(self, position):
        """Returns a list of valid moves for the Bishop from the given position (row, col)."""
        row, col = position
        moves = []

        # Diagonal moves in all four directions
        for i in range(1, 8):
            # Up-Right
            if row - i >= 0 and col + i < 8:
                moves.append((row - i, col + i))
            # Up-Left
            if row - i >= 0 and col - i >= 0:
                moves.append((row - i, col - i))
            # Down-Right
            if row + i < 8 and col + i < 8:
                moves.append((row + i, col + i))
            # Down-Left
            if row + i < 8 and col - i >= 0:
                moves.append((row + i, col - i))
        
        return moves
