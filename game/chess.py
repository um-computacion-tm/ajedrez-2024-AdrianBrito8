
from .board import Board
from .exceptions import InvalidMove, InvalidTurn, EmptyPosition
from game.pawn import Pawn

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def is_playing(self):
        return True

    def move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if piece is None:
            raise EmptyPosition("No piece at the starting position.")

        if not hasattr(piece, 'get_color'):
            raise AttributeError("The piece does not have a color attribute.")

        if piece.get_color() != self.turn:
            raise InvalidTurn("It's not the turn of the player who owns the piece.")

        if (to_row, to_col) not in piece.valid_moves((from_row, from_col), self.__board__):

            raise InvalidMove("Move is not valid for the piece.")

        self.__board__.move_piece(from_row, from_col, to_row, to_col)

        if isinstance(piece, Pawn):
            if (piece.get_color() == "WHITE" and to_row == 0) or (piece.get_color() == "BLACK" and to_row == 7):
                choice = input("Promote pawn to (queen/rook/bishop/knight): ").strip().lower()
                try:
                    promoted_piece = piece.promote(choice)
                    self.__board__.place_piece(promoted_piece, to_row, to_col)
                except ValueError as e:
                    print(f"Error: {e}")
                    self.__board__.move_piece(to_row, to_col, from_row, from_col)
                    raise
        else:
            self.change_turn()

    @property
    def turn(self):
        return self.__turn__

    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"
