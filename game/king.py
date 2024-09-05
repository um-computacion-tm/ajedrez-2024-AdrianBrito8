from game.piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return f"K({self.get_color()[0]})"

    def valid_moves(self, position, board):
        row, col = position
        potential_moves = [
            (row + 1, col), (row - 1, col),  # Vertical moves
            (row, col + 1), (row, col - 1),  # Horizontal moves
            (row + 1, col + 1), (row - 1, col - 1),  # Diagonal moves
            (row + 1, col - 1), (row - 1, col + 1)   # Diagonal moves
        ]
        valid_moves = []

        
        for move in potential_moves:
            if 0 <= move[0] < 8 and 0 <= move[1] < 8:
                if board.is_empty_position(*move) or board.get_piece(*move).get_color() != self.get_color():
                    valid_moves.append(move)

        return valid_moves
