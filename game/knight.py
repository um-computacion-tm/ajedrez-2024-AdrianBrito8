class Knight:
    def __init__(self, color, position=None):
        self.color = color
        self.position = position

    def get_color(self):
        return self.color

    def set_position(self, position):
        self.position = position

    def __str__(self):
        color_initial = "W" if self.color == "WHITE" else "B"
        return f"N({color_initial})"

    def valid_moves(self, position, board=None):
        row, col = position
        moves = []

        potential_moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2),
        ]

        for r, c in potential_moves:
            if 0 <= r < 8 and 0 <= c < 8:
                # Check if position is empty or has an enemy piece
                if board.is_empty_position(r, c) or board.get_piece(r, c).get_color() != self.color:
                    moves.append((r, c))
        
        return moves

    def can_attack(self, target_position, board):
        # Ensure target_position is valid and contains an enemy piece
        if target_position in self.valid_moves(self.position, board):
            target_piece = board.get_piece(*target_position)
            return target_piece is not None and target_piece.get_color() != self.color
        return False
