import unittest
from game.knight import Knight

class TestKnight(unittest.TestCase):
    def test_knight_color(self):
        knight_white = Knight("WHITE")
        self.assertEqual(knight_white.get_color(), "WHITE")
        
        knight_black = Knight("BLACK")
        self.assertEqual(knight_black.get_color(), "BLACK")
    
    def test_knight_str(self):
        knight_white = Knight("WHITE")
        self.assertEqual(str(knight_white), "N(W)")
        
        knight_black = Knight("BLACK")
        self.assertEqual(str(knight_black), "N(B)")
    
    def test_knight_valid_moves(self):
        knight = Knight("WHITE")
        
        # Position at (0, 1)
        moves = knight.valid_moves((0, 1))
        expected_moves = [(2, 0), (2, 2), (1, 3)]
        self.assertCountEqual(moves, expected_moves)
        
        # Position at (3, 3)
        moves = knight.valid_moves((3, 3))
        expected_moves = [
            (5, 4), (5, 2), (1, 4), (1, 2), 
            (4, 5), (4, 1), (2, 5), (2, 1)
        ]
        self.assertCountEqual(moves, expected_moves)

if __name__ == '__main__':
    unittest.main()

