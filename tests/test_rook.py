import unittest
from game.rook import Rook

class TestRook(unittest.TestCase):
    def test_rook_color(self):
        rook_white = Rook("WHITE")
        self.assertEqual(rook_white.get_color(), "WHITE")
        
        rook_black = Rook("BLACK")
        self.assertEqual(rook_black.get_color(), "BLACK")

    def test_rook_str(self):
        rook_white = Rook("WHITE")
        self.assertEqual(str(rook_white), "R(W)")
        
        rook_black = Rook("BLACK")
        self.assertEqual(str(rook_black), "R(B)")

    def test_rook_valid_moves(self):
        rook = Rook("BLACK")
        
        # Position at (0, 0)
        moves = rook.valid_moves((0, 0))
        expected_moves = [(0, i) for i in range(1, 8)] + [(i, 0) for i in range(1, 8)]
        self.assertCountEqual(moves, expected_moves)
        
        # Position at (3, 3)
        moves = rook.valid_moves((3, 3))
        expected_moves = [(3, i) for i in range(8) if i != 3] + [(i, 3) for i in range(8) if i != 3]
        self.assertCountEqual(moves, expected_moves)

if __name__ == '__main__':
    unittest.main()
