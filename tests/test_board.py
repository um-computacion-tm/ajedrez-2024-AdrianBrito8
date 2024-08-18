import unittest
from game.board import Board
from game.rook import Rook

class TestBoard(unittest.TestCase):
    def test_board_initial_positions(self):
        board = Board()

        self.assertIsInstance(board.get_piece(0, 0), Rook)
        self.assertEqual(board.get_piece(0, 0).get_color(), "BLACK")
        
        self.assertIsInstance(board.get_piece(0, 7), Rook)
        self.assertEqual(board.get_piece(0, 7).get_color(), "BLACK")
        
        self.assertIsInstance(board.get_piece(7, 0), Rook)
        self.assertEqual(board.get_piece(7, 0).get_color(), "WHITE")
        
        self.assertIsInstance(board.get_piece(7, 7), Rook)
        self.assertEqual(board.get_piece(7, 7).get_color(), "WHITE")

    def test_get_piece_out_of_bounds(self):
        board = Board()

        with self.assertRaises(IndexError):
            board.get_piece(-1, 0)

        with self.assertRaises(IndexError):
            board.get_piece(8, 0)

        with self.assertRaises(IndexError):
            board.get_piece(0, 8)

if __name__ == '__main__':
    unittest.main()
