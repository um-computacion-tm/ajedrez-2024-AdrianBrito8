import unittest
from game.chess import Chess
from game.pawn import Pawn
from game.queen import Queen
from game.rook import Rook
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition
from unittest.mock import patch

class TestChess(unittest.TestCase):
    def setUp(self):
        self.game = Chess()
        self.game.__board__.place_piece(Rook("WHITE"), 0, 0)
        self.game.__board__.place_piece(Pawn("WHITE"), 1, 0)
        self.game.__board__.place_piece(Rook("BLACK"), 0, 1)


    def test_initial_turn(self):
        self.assertEqual(self.game.turn, "WHITE")

    def test_change_turn(self):
        self.game.change_turn()
        self.assertEqual(self.game.turn, "BLACK")
    
    def test_move_empty_position(self):
        self.game.__board__.place_piece(Rook("WHITE"), 0, 0)
        self.assertIsNone(self.game.__board__.get_piece(2, 2), "Position (2, 2) should be empty")
        with self.assertRaises(EmptyPosition, msg="Expected EmptyPosition exception"):
            self.game.move(0, 0, 2, 2)

    def test_invalid_turn(self):
        self.game.__board__.place_piece(Rook("BLACK"), 0, 0)
        self.game.change_turn()  # Cambia el turno a "WHITE"
        self.assertIsInstance(self.game.__board__.get_piece(0, 0), Rook, "Expected Rook at (0, 0)")
        with self.assertRaises(InvalidTurn, msg="Expected InvalidTurn exception"):
            self.game.move(0, 0, 1, 0)

    @patch('builtins.input', return_value='queen')
    def test_pawn_promotion(self, mock_input):
        self.game.__board__.place_piece(Pawn("WHITE"), 1, 0)
        self.assertIsInstance(self.game.__board__.get_piece(1, 0), Pawn, "Expected Pawn at (1, 0)")
        self.game.move(1, 0, 0, 0)  # Movemos el peón a la fila de promoción
        promoted_piece = self.game.__board__.get_piece(0, 0)
        self.assertIsInstance(promoted_piece, Queen, "Pawn should be promoted to Queen")

if __name__ == "__main__":
    unittest.main()
