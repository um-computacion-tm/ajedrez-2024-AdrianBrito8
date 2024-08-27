from .piece import Piece


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__moved__ = False  
        
    def valid_moves(self, position):
        
        row, col = position
        moves = []

        if self.get_color() == "WHITE":
            direction = -1  # Peón blanco se mueve hacia arriba en el tablero
        else:
            direction = 1  # Peón negro se mueve hacia abajo en el tablero

        # Movimiento hacia adelante
        forward_move = (row + direction, col)
        if 0 <= forward_move[0] < 8:  
            moves.append(forward_move)

        # Movimiento doble hacia adelante si no ha movido
        if not self.__moved__:
            double_forward_move = (row + 2 * direction, col)
            if 0 <= double_forward_move[0] < 8:
                moves.append(double_forward_move)

        # Captura en diagonal
        for diagonal_col in [col - 1, col + 1]:
            diagonal_move = (row + direction, diagonal_col)
            if 0 <= diagonal_move[0] < 8 and 0 <= diagonal_move[1] < 8:
                moves.append(diagonal_move)

        return moves

    def move(self):
        self.__moved__ = True
