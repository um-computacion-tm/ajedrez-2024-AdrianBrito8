import unittest
from game.chess import Chess
from game.pawn import Pawn
from game.queen import Queen
from game.rook import Rook
from game.bishop import Bishop
from game.knight import Knight
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition

class TestChess(unittest.TestCase):
    def setUp(self):
        self.game = Chess()

    def test_valid_move(self):
        # Coloca un peón blanco en la posición inicial
        self.game.board.place_piece(Pawn("WHITE"), 6, 0)
        self.game.move(6, 0, 5, 0)
        self.assertIsInstance(self.game.board.get_piece(5, 0), Pawn)
        self.assertEqual(self.game.board.get_piece(5, 0).get_color(), "WHITE")

    def test_invalid_move(self):
        
        self.game.move(6, 0, 5, 0)  # Mueve un peón blanco para dejar la posición (6, 0) vacía
        with self.assertRaises(EmptyPosition):
            self.game.move(0, 0, 1, 0)  # Ahora la posición (0, 0) debería estar vacía

    def test_invalid_turn(self):
        self.game.move(6, 0, 5, 0)  # Mueve un peón blanco
        with self.assertRaises(InvalidTurn):
            self.game.move(5, 0, 4, 0)  # Intentar mover el peón blanco en el turno negro

    def test_pawn_promotion_to_queen(self):
        # Coloca un peón blanco en la fila 6
        self.game.board.place_piece(Pawn("WHITE"), 6, 0)
        self.game.move(6, 0, 0, 0, promotion_choice='queen')
        self.assertIsInstance(self.game.board.get_piece(0, 0), Queen)
        self.assertEqual(self.game.board.get_piece(0, 0).get_color(), "WHITE")

    def test_pawn_promotion_to_rook(self):
        # Coloca un peón blanco en la fila 6
        self.game.board.place_piece(Pawn("WHITE"), 6, 1)
        self.game.move(6, 1, 0, 1, promotion_choice='rook')
        self.assertIsInstance(self.game.board.get_piece(0, 1), Rook)
        self.assertEqual(self.game.board.get_piece(0, 1).get_color(), "WHITE")

    def test_pawn_promotion_to_bishop(self):
        # Coloca un peón blanco en la fila 6
        self.game.board.place_piece(Pawn("WHITE"), 6, 2)
        self.game.move(6, 2, 0, 2, promotion_choice='bishop')
        self.assertIsInstance(self.game.board.get_piece(0, 2), Bishop)
        self.assertEqual(self.game.board.get_piece(0, 2).get_color(), "WHITE")

    def test_pawn_promotion_to_knight(self):
        # Coloca un peón blanco en la fila 6
        self.game.board.place_piece(Pawn("WHITE"), 6, 3)
        self.game.move(6, 3, 0, 3, promotion_choice='knight')
        self.assertIsInstance(self.game.board.get_piece(0, 3), Knight)
        self.assertEqual(self.game.board.get_piece(0, 3).get_color(), "WHITE")

    def test_invalid_pawn_promotion_choice(self):
        # Coloca un peón blanco en la fila 6
        self.game.board.place_piece(Pawn("WHITE"), 6, 0)
        with self.assertRaises(ValueError):
            self.game.move(6, 0, 0, 0, promotion_choice='invalid_choice')

if __name__ == '__main__':
    unittest.main()
