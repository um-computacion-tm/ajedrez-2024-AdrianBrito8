from game.piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return "K" if self.get_color() == "WHITE" else "k"

    def valid_moves(self, position, board=None):
        row, col = position
        potential_moves = [
            (row + 1, col), (row - 1, col),  # Vertical moves
            (row, col + 1), (row, col - 1),  # Horizontal moves
            (row + 1, col + 1), (row - 1, col - 1),  # Diagonal moves
            (row + 1, col - 1), (row - 1, col + 1)   # Diagonal moves
        ]
        valid_moves = []

        for move in potential_moves:
            if self.is_on_board(move) and self.is_enemy_or_empty(move, board):
                valid_moves.append(move)

        return valid_moves

    def is_on_board(self, position):
        row, col = position
        return 0 <= row < 8 and 0 <= col < 8

    def move(self, new_position, board):
        if new_position in self.valid_moves(self.get_position(), board):
            current_row, current_col = self.get_position()
            new_row, new_col = new_position
            board.move_piece(current_row, current_col, new_row, new_col)
            self.set_position(new_position)
            return True
        return False

    def can_attack(self, position, board):
        return position in self.valid_moves(self.get_position(), board)