import unittest
from game.queen import Queen

class TestQueen(unittest.TestCase):
    def test_queen_color(self):
        queen_white = Queen("WHITE")
        self.assertEqual(queen_white.get_color(), "WHITE")
        
        queen_black = Queen("BLACK")
        self.assertEqual(queen_black.get_color(), "BLACK")
    
    def test_queen_str(self):
        queen_white = Queen("WHITE")
        self.assertEqual(str(queen_white), "Q(W)")
        
        queen_black = Queen("BLACK")
        self.assertEqual(str(queen_black), "Q(B)")
    
    def test_queen_valid_moves_center(self):
        queen = Queen("WHITE")
        position = (4, 4)
        moves = queen.valid_moves(position)
        
        expected_moves = [
            # Horizontal moves
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7),
            # Vertical moves
            (0, 4), (1, 4), (2, 4), (3, 4), (5, 4), (6, 4), (7, 4),
            # Diagonal moves
            (3, 5), (2, 6), (1, 7), (3, 3), (2, 2), (1, 1), (0, 0),
            (5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1)
        ]
        
        self.assertCountEqual(moves, expected_moves)
    
    def test_queen_valid_moves_corner(self):
        queen = Queen("BLACK")
        position = (0, 0)
        moves = queen.valid_moves(position)
        
        expected_moves = [
            # Horizontal moves
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
            # Vertical moves
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            # Diagonal moves
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)
        ]
        
        self.assertCountEqual(moves, expected_moves)

if __name__ == '__main__':
        unittest.main()
