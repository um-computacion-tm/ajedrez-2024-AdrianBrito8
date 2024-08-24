import unittest
from game.piece import Piece

class TestPiece(unittest.TestCase):
    def test_piece_color(self):
        piece = Piece("WHITE")
        self.assertEqual(piece.get_color(), "WHITE")
        piece_black = Piece("BLACK")
        self.assertEqual(piece_black.get_color(), "BLACK")
    
    def test_piece_str(self):
        piece = Piece("WHITE")
        self.assertEqual(str(piece), "Piece(WHITE)")
        piece_black = Piece("BLACK")
        self.assertEqual(str(piece_black), "Piece(BLACK)")

    def test_is_opponent_piece(self):
        white_piece = Piece("WHITE")
        black_piece = Piece("BLACK")

        self.assertTrue(white_piece.is_opponent_piece(black_piece))
        self.assertTrue(black_piece.is_opponent_piece(white_piece))
        self.assertFalse(white_piece.is_opponent_piece(Piece("WHITE")))
        self.assertFalse(black_piece.is_opponent_piece(Piece("BLACK")))

    def test_move_to(self):
        piece = Piece("WHITE")
        
        self.assertIsNone(piece.get_position())
        
        piece.move_to((3, 3))
        self.assertEqual(piece.get_position(), (3, 3))
        
        piece.move_to((5, 5))
        self.assertEqual(piece.get_position(), (5, 5))

    def test_capture_piece(self):
        piece = Piece("WHITE")

        self.assertFalse(piece.is_captured())     
        piece.capture()
        
        self.assertTrue(piece.is_captured())


if __name__ == '__main__':
    unittest.main()
