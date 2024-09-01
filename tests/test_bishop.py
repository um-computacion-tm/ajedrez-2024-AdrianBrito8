import unittest
from game.bishop import Bishop

class TestBishop(unittest.TestCase):
    def test_bishop_color(self):
        bishop_white = Bishop("WHITE")
        self.assertEqual(bishop_white.get_color(), "WHITE")
        
        bishop_black = Bishop("BLACK")
        self.assertEqual(bishop_black.get_color(), "BLACK")
    
    def test_bishop_str(self):
        bishop_white = Bishop("WHITE")
        self.assertEqual(str(bishop_white), "B(W)")
        
        bishop_black = Bishop("BLACK")
        self.assertEqual(str(bishop_black), "B(B)")
    
    def test_bishop_valid_moves_center(self):
        bishop = Bishop("WHITE")
        position = (4, 4)
        moves = bishop.valid_moves(position)
        
        expected_moves = [
            (3, 5), (2, 6), (1, 7),             # Up-Right
            (3, 3), (2, 2), (1, 1), (0, 0),     # Up-Left
            (5, 5), (6, 6), (7, 7),             # Down-Right
            (5, 3), (6, 2), (7, 1)              # Down-Left
        ]
        
        self.assertCountEqual(moves, expected_moves)
    
    def test_bishop_valid_moves_corner(self):
        bishop = Bishop("BLACK")
        position = (0, 0)
        moves = bishop.valid_moves(position)
        
        expected_moves = [
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)  # Down-Right
        ]
        
        self.assertCountEqual(moves, expected_moves)

if __name__ == '__main__':
    unittest.main()
