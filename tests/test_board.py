import unittest
from game.board import Board
from game.rook import Rook
from game.pawn import Pawn
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.king import King
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
    
    def test_board_initial_positions(self):
        # Check black rooks
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertEqual(self.board.get_piece(0, 0).get_color(), "BLACK")
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertEqual(self.board.get_piece(0, 7).get_color(), "BLACK")

        # Check white rooks
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertEqual(self.board.get_piece(7, 0).get_color(), "WHITE")
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        self.assertEqual(self.board.get_piece(7, 7).get_color(), "WHITE")

        # Check pawns
        for col in range(8):
            self.assertIsInstance(self.board.get_piece(1, col), Pawn)
            self.assertEqual(self.board.get_piece(1, col).get_color(), "BLACK")
            self.assertIsInstance(self.board.get_piece(6, col), Pawn)
            self.assertEqual(self.board.get_piece(6, col).get_color(), "WHITE")

        # Check other black pieces
        self.assertIsInstance(self.board.get_piece(0, 3), Queen)
        self.assertIsInstance(self.board.get_piece(0, 4), King)
        
        # Check other white pieces
        self.assertIsInstance(self.board.get_piece(7, 3), Queen)
        self.assertIsInstance(self.board.get_piece(7, 4), King)

    def test_get_piece_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.board.get_piece(-1, 0)
        with self.assertRaises(IndexError):
            self.board.get_piece(8, 0)
        with self.assertRaises(IndexError):
            self.board.get_piece(0, 8)

    def test_move_piece(self):
        # Move a white pawn from (6, 0) to (4, 0)
        self.board.move_piece(6, 0, 4, 0)
        self.assertIsNone(self.board.get_piece(6, 0))
        self.assertIsInstance(self.board.get_piece(4, 0), Pawn)
        self.assertEqual(self.board.get_piece(4, 0).get_color(), "WHITE")

        # Black's turn: move a black pawn from (1, 0) to (3, 0)
        self.board.move_piece(1, 0, 3, 0)
        self.assertIsNone(self.board.get_piece(1, 0))
        self.assertIsInstance(self.board.get_piece(3, 0), Pawn)
        self.assertEqual(self.board.get_piece(3, 0).get_color(), "BLACK")

        # White's turn : move a white rook from (7, 7) to (5, 7)
        self.board.move_piece(7, 7, 5, 7)
        self.assertIsNone(self.board.get_piece(7, 7))
        self.assertIsInstance(self.board.get_piece(5, 7), Rook)
        self.assertEqual(self.board.get_piece(5, 7).get_color(), "WHITE")

        # Attempt an invalid move for the black rook (0, 7) to (1, 6) (should fail)
        with self.assertRaises(InvalidMove):
            self.board.move_piece(0, 7, 1, 6)

    def test_move_piece_out_of_bounds(self):
        with self.assertRaises(IndexError):
            self.board.move_piece(0, 0, 8, 8)

    def test_is_empty_position(self):
        self.assertTrue(self.board.is_empty_position(3, 3))
        self.assertTrue(self.board.is_empty_position(4, 4))

        self.assertFalse(self.board.is_empty_position(0, 0))
        self.assertFalse(self.board.is_empty_position(7, 7))

        with self.assertRaises(IndexError):
            self.board.is_empty_position(-1, 0)
        with self.assertRaises(IndexError):
            self.board.is_empty_position(8, 0)
        with self.assertRaises(IndexError):
            self.board.is_empty_position(0, 8)

    def test_remove_piece(self):
        # Place a white pawn at (6, 0)
        self.board.place_piece(Pawn("WHITE"), 6, 0)
        self.assertIsInstance(self.board.get_piece(6, 0), Pawn)
        self.assertEqual(self.board.get_piece(6, 0).get_color(), "WHITE")

        # Remove the white pawn from (6, 0)
        self.board.remove_piece(6, 0)
        self.assertIsNone(self.board.get_piece(6, 0))

        with self.assertRaises(IndexError):
            self.board.remove_piece(-1, 0)
        with self.assertRaises(IndexError):
            self.board.remove_piece(8, 0)
        with self.assertRaises(IndexError):
            self.board.remove_piece(0, 8)

class TestBoardShow(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_board(self):
        expected_board = (
            "8 r n b q k b n r \n"
            "7 p p p p p p p p \n"
            "6 . . . . . . . . \n"
            "5 . . . . . . . . \n"
            "4 . . . . . . . . \n"
            "3 . . . . . . . . \n"
            "2 P P P P P P P P \n"
            "1 R N B Q K B N R \n"
            "  a b c d e f g h\n"
        )
        self.assertEqual(self.board.show_board(), expected_board)

    def test_board_after_move(self):
        # Move a white pawn from e2 to e4
        self.board.move_piece(6, 4, 4, 4)  # e2 -> e4

        expected_board_after_move = (
            "8 r n b q k b n r \n"
            "7 p p p p p p p p \n"
            "6 . . . . . . . . \n"
            "5 . . . . . . . . \n"
            "4 . . . . P . . . \n"
            "3 . . . . . . . . \n"
            "2 P P P P . P P P \n"
            "1 R N B Q K B N R \n"
            "  a b c d e f g h\n"
        )
        self.assertEqual(self.board.show_board(), expected_board_after_move)

    def test_get_king_position(self):
        # Create an empty board
        board = Board()

        # Remove the black king from (0, 4)
        board.remove_piece(0, 4)

        # Remove the white king from (7, 4)
        board.remove_piece(7, 4)

        # Place a white king at (0, 0)
        king_white = King("WHITE")
        board.set_piece((0, 0), king_white)

        # Verify the white king's position is (0, 0)
        self.assertEqual(board.get_king_position("WHITE"), (0, 0))

        # Place a black king at (5, 5)
        king_black = King("BLACK")
        board.set_piece((5, 5), king_black)

        # Verify the black king's position is (5, 5)
        self.assertEqual(board.get_king_position("BLACK"), (5, 5))

        # Place a white pawn at ( 0, 0)
        pawn_white = Pawn("WHITE")
        board.set_piece((0, 0), pawn_white)

        # Verify the white king's position is None
        self.assertIsNone(board.get_king_position("WHITE"))

        # Place a white king at (0, 0)
        king_white = King("WHITE")
        board.set_piece((0, 0), king_white)

        # Verify the white king's position is (0, 0)
        self.assertEqual(board.get_king_position("WHITE"), (0, 0))

class TestBoardPathIsClear(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        # Clear any existing pieces to avoid interference
        for row in range(8):
            for col in range(8):
                self.board.remove_piece(row, col)

    def test_path_is_clear_horizontal(self):
        # Clear path from (7, 0) to (7, 3)
        self.assertTrue(self.board.path_is_clear((7, 0), (7, 3)))
        # Place a piece at (7, 1) to block the path
        self.board.place_piece(Rook("WHITE"), 7, 1)
        self.assertFalse(self.board.path_is_clear((7, 0), (7, 3)))

        # Remove the blocking piece and check again
        self.board.remove_piece(7, 1)
        self.assertTrue(self.board.path_is_clear((7, 0), (7, 3)))

    def test_path_is_clear_vertical(self):
        # Clear path from (6, 0) to (1, 0)
        self.assertTrue(self.board.path_is_clear((6, 0), (1, 0)))

        # Place a piece at (5, 0) to block the path
        self.board.place_piece(Rook("WHITE"), 5, 0)
        self.assertFalse(self.board.path_is_clear((6, 0), (1, 0)))

        # Remove the blocking piece and check again
        self.board.remove_piece(5, 0)
        self.assertTrue(self.board.path_is_clear((6, 0), (1, 0)))

    def test_path_is_clear_diagonal(self):
        # Check that the method returns False for diagonal moves
        self.assertFalse(self.board.path_is_clear((7, 0), (5, 2)))

    def test_path_is_clear_with_edge_of_board(self):
        # Test with edges of the board
        self.assertTrue(self.board.path_is_clear((7, 0), (7, 7)))  # Clear path horizontally
        self.assertTrue(self.board.path_is_clear((0, 0), (7, 0)))  # Clear path vertically

        # Block the path with a piece at (3, 0)
        self.board.place_piece(Rook("WHITE"), 3, 0)
        self.assertFalse(self.board.path_is_clear((0, 0), (7, 0)))  # Now the path is blocked

    def test_path_is_clear_empty_path(self):
        # Check an empty path
        self.assertTrue(self.board.path_is_clear((4, 4), (4, 7)))  # Horizontal
        self.assertTrue(self.board.path_is_clear((4, 4), (1, 4)))  # Vertical

if __name__ == '__main__':
    unittest.main()