from game.piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        if self.get_color() == "WHITE":
            return "K"
        else:
            return "k"

    def valid_moves(self, position, board=None, check_check=True):
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
                    # Verificar si el movimiento pone al rey en jaque (solo si check_check=True)
                    if not check_check or not self.is_in_check(move, board):
                        valid_moves.append(move)

        return valid_moves
    
    def is_in_check(self, position, board):
        enemy_color = "BLACK" if self.get_color() == "WHITE" else "WHITE"
        # Recorrer todas las piezas del tablero para verificar si alguna puede atacar la posición del rey
        for r in range(8):
            for c in range(8):
                piece = board.get_piece(r, c)
                if piece and piece.get_color() == enemy_color:
                    if position in piece.valid_moves((r, c), board):
                        return True
        return False
    
    def can_attack(self, position, board):
        return position in self.valid_moves(self.get_position(), board)
