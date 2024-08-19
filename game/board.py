from .rook import Rook

class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__[0][0] = Rook("BLACK") # Black
        self.__positions__[0][7] = Rook("BLACK") # Black
        self.__positions__[7][7] = Rook("WHITE") # White
        self.__positions__[7][0] = Rook("WHITE") # White

    def get_piece(self, row, col):
        if 0 <= row < 8 and 0 <= col < 8:
            return self.__positions__[row][col]
        else:
            raise IndexError("Position out of board range.")

    def move_piece(self, start_row, start_col, end_row, end_col):
        if 0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8:
            piece = self.__positions__[start_row][start_col]
            self.__positions__[start_row][start_col] = None
            self.__positions__[end_row][end_col] = piece
        else:
            raise IndexError("Move out of board range.")