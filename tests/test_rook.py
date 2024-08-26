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

    def test_rook_valid_moves_edge_case(self):
        rook = Rook("WHITE")
        
        moves = rook.valid_moves((7, 7))
        expected_moves = [(7, i) for i in range(7)] + [(i, 7) for i in range(7)]
        self.assertCountEqual(moves, expected_moves)

    def test_rook_valid_moves_central_position(self):
        rook = Rook("WHITE")
        
        # Position at (4, 4)
        moves = rook.valid_moves((4, 4))
        expected_moves = [(4, i) for i in range(8) if i != 4] + [(i, 4) for i in range(8) if i != 4]
        self.assertCountEqual(moves, expected_moves)

    def test_rook_can_attack(self):
        rook = Rook("BLACK")

        # Rook at (0, 0)
        self.assertTrue(rook.can_attack((0, 0), (0, 7)))  # Same row
        self.assertTrue(rook.can_attack((0, 0), (7, 0)))  # Same column
        self.assertFalse(rook.can_attack((0, 0), (7, 7)))  # Not in the same row/column



if __name__ == '__main__':
    unittest.main()
