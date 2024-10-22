from game.rook import Rook
from game.queen import Queen
from game.bishop import Bishop
from game.knight import Knight
from game.king import King
from game.pawn import Pawn
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition

class Board:
    def __init__(self):
        # Initialize the board with empty positions
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.setup_initial_pieces()
        self.current_turn = "WHITE"

    def setup_initial_pieces(self):
        # Place pawns
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK")
            self.__positions__[6][col] = Pawn("WHITE")
    
        # Place rooks
        self.__positions__[0][0] = Rook("BLACK")
        self.__positions__[0][7] = Rook("BLACK")
        self.__positions__[7][0] = Rook("WHITE")
        self.__positions__[7][7] = Rook("WHITE")

        # Place knights
        self.__positions__[0][1] = Knight("BLACK")
        self.__positions__[0][6] = Knight("BLACK")
        self.__positions__[7][1] = Knight("WHITE")
        self.__positions__[7][6] = Knight("WHITE")

        # Place bishops
        self.__positions__[0][2] = Bishop("BLACK")
        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[7][2] = Bishop("WHITE")
        self.__positions__[7][5] = Bishop("WHITE")

        # Place queens
        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[7][3] = Queen("WHITE")

        # Place kings
        self.__positions__[0][4] = King("BLACK")
        self.__positions__[7][4] = King("WHITE")


    def get_piece(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return self.__positions__[row][col]
        else:
            raise IndexError("Position out of board range.")

    def move_piece(self, start_row, start_col, end_row, end_col):
        if not self._in_bounds(start_row, start_col) or not self._in_bounds(end_row, end_col):
            raise IndexError("Move out of board range.")

        piece = self.get_piece(start_row, start_col)
        if piece is None:
            raise EmptyPosition("No piece at the source position.")

        # Check if it's the correct turn
        if piece.get_color() != self.current_turn:
            raise InvalidTurn("It's not your turn.")

        # Check if the move is valid for the piece
        valid_moves = piece.valid_moves((start_row, start_col), self)
        if (end_row, end_col) not in valid_moves:
            raise InvalidMove("Invalid move for the piece.")

        # Perform the move
        self.__positions__[start_row][start_col] = None
        self.__positions__[end_row][end_col] = piece

        # Change the turn
        self.current_turn = "WHITE" if self.current_turn == "BLACK" else "BLACK"

    def is_empty_position(self, row, col):
        if self._in_bounds(row, col):
            return self.__positions__[row][col] is None
        else:
            raise IndexError("Position out of board range.")
    
    def is_enemy_piece(self, piece, position):
        row, col = position
        target_piece = self.get_piece(row, col)
        return target_piece is not None and target_piece.get_color() != piece.get_color()
    
    def _in_bounds(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def update_position(self, position, piece=None):
        row, col = position
        if self._in_bounds(row, col):
            self.__positions__[row][col] = piece
        else:
            raise IndexError("Position out of board range.")

    def place_piece(self, piece, row, col):
        self.update_position((row, col), piece)

    def set_piece(self, position, piece):
        self.update_position(position, piece)

    def remove_piece(self, row, col):
        self.update_position((row, col), None)

    def get_pieces(self, color):
        return [piece for row in self.__positions__ for piece in row if piece is not None and piece.get_color() == color]

    def show_board(self):
        board_str = ""
        for row in range(8):
            board_str += str(8 - row) + " "  # Show row numbers from 8 to 1
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece is None:
                    board_str += ". "  # Empty square
                else:
                    if piece.get_color() == "WHITE":
                        board_str += str(piece).upper() + " "
                    else:
                        board_str += str(piece).lower() + " "

            board_str += "\n"
            
        board_str += "  a b c d e f g h\n"  # Show column letters from 'a' to 'h'
        return board_str
    
    def path_is_clear(self, start, end):
        """Verifica si el camino de start a end está libre de obstrucciones."""
        row_start, col_start = start
        row_end, col_end = end

        # Movimiento en la misma fila (horizontal)
        if row_start == row_end:
            step = 1 if col_end > col_start else -1
            for col in range(col_start + step, col_end, step):
                if self.get_piece(row_start, col) is not None:
                    return False
            return True
        
        # Movimiento en la misma columna (vertical)
        elif col_start == col_end:
            step = 1 if row_end > row_start else -1
            for row in range(row_start + step, row_end, step):
                if self.get_piece(row, col_start) is not None:
                    return False
            return True

        return False


    def get_king_position(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece is not None and isinstance(piece, King) and piece.get_color() == color:
                    return (row, col)


        return None