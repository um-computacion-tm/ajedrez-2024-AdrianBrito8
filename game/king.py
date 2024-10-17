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
            if self.is_enemy_or_empty(move, board):
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
    
    def move(self, new_position, board):
        if new_position in self.valid_moves(self.get_position(), board):
            # Obtener la posición actual del rey
            current_row, current_col = self.get_position()
            new_row, new_col = new_position
        
            # Mover la pieza en el tablero descomponiendo la tupla en fila y columna
            board.move_piece(current_row, current_col, new_row, new_col)
        
            # Actualizar la posición del rey
            self.set_position(new_position)
            return True
        return False
    
    def can_attack(self, position, board):
        return position in self.valid_moves(self.get_position(), board)
