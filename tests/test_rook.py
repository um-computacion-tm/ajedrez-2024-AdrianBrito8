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

if __name__ == '__main__':
    unittest.main()
