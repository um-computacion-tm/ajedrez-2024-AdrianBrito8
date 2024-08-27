import unittest
from game.pawn import Pawn

class TestPawn(unittest.TestCase):
    def test_pawn_valid_moves(self):
        pawn_white = Pawn("WHITE")
        pawn_black = Pawn("BLACK")

        # Blancas inicia
        moves = pawn_white.valid_moves((6, 4))
        expected_moves = [(5, 4), (4, 4), (5, 3), (5, 5)]
        self.assertCountEqual(moves, expected_moves)

        # Negras inicia
        moves = pawn_black.valid_moves((1, 4))
        expected_moves = [(2, 4), (3, 4), (2, 3), (2, 5)]
        self.assertCountEqual(moves, expected_moves)

        pawn_white.move()
        moves = pawn_white.valid_moves((5, 4))
        expected_moves = [(4, 4), (4, 3), (4, 5)]
        self.assertCountEqual(moves, expected_moves)

        pawn_black.move()
        moves = pawn_black.valid_moves((2, 4))
        expected_moves = [(3, 4), (3, 3), (3, 5)]
        self.assertCountEqual(moves, expected_moves)

if __name__ == '__main__':
    unittest.main()
