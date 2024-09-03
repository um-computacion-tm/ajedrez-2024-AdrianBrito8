from .piece import Piece

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
    
    def __str__(self):
        return f"N({self.get_color()[0]})"
    
    def valid_moves(self, position):
        """Returns a list of valid moves for the Knight from the given position (row, col)."""
        row, col = position
        moves = []
        
        # Possible moves for a knight in terms of (row, col) changes
        possible_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        
        for move in possible_moves:
            new_row, new_col = row + move[0], col + move[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                moves.append((new_row, new_col))
        
        return moves
