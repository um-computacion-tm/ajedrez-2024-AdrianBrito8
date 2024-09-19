from .piece import Piece

class Rook(Piece):
    def __init__(self, color, position=None):
        super().__init__(color)
        self.position = position

    def __str__(self):
        return f"R({self.get_color()[0]})"

    def valid_moves(self, position, board=None):
        row, col = position
        moves = []

        # Movimientos en la misma fila
        for i in range(8):
            if i != col:
                moves.append((row, i))

        # Movimientos en la misma columna
        for i in range(8):
            if i != row:
                moves.append((i, col))

        return moves

    def can_attack(self, target_position, board):
        """
        Verifica si la torre puede atacar una pieza enemiga en la posición objetivo.
        """
        if target_position in self.valid_moves(self.position, board):
            target_piece = board.get_piece(*target_position)
            if target_piece and target_piece.get_color() != self.get_color():
                return True
        return False
