import unittest
from game.king import King
from game.board import Board
from game.rook import Rook

class TestKing(unittest.TestCase):
    def test_king_color(self):
        king_white = King("WHITE")
        self.assertEqual(king_white.get_color(), "WHITE")
        
        king_black = King("BLACK")
        self.assertEqual(king_black.get_color(), "BLACK")

    def test_king_str(self):
        king_white = King("WHITE")
        self.assertEqual(str(king_white), "K(W)")
        
        king_black = King("BLACK")
        self.assertEqual(str(king_black), "K(B)")

    def test_king_valid_moves(self):
        king = King("BLACK")
        board = Board()
        moves = king.valid_moves((4, 4), board)

        expected_moves = [
            (5, 4), (3, 4), (4, 5), (4, 3),
            (5, 5), (3, 3), (5, 3), (3, 5)
        ]
        self.assertCountEqual(moves, expected_moves)

        def test_king_can_attack(self):
            board = Board()
            king = King("WHITE")
            board.place_piece(king, 4, 4)

            # Test attack on an enemy piece (should attack)
            enemy_piece = Rook("BLACK")
            board.place_piece(enemy_piece, 5, 5)
            self.assertIn((5, 5), king.valid_moves((4, 4), board))

            # Test that it cannot attack a friendly piece (should not attack)
            friendly_piece = Rook("WHITE")
            board.place_piece(friendly_piece, 3, 3)
            self.assertNotIn((3, 3), king.valid_moves((4, 4), board))


if __name__ == '__main__':
    unittest.main()
