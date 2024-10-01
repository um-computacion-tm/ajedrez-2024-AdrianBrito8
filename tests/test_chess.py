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
        # Coloca un peón blanco en la posición inicial y lo mueve hacia adelante
        self.game.board.place_piece(Pawn("WHITE"), 6, 0)
        self.game.move(6, 0, 5, 0)
        self.assertIsInstance(self.game.board.get_piece(5, 0), Pawn)
        self.assertEqual(self.game.board.get_piece(5, 0).get_color(), "WHITE")
        self.assertIsNone(self.game.board.get_piece(6, 0))

    def test_invalid_move(self):
        # Coloca un peón blanco en la posición inicial
        self.game.board.place_piece(Pawn("WHITE"), 6, 0)

        # Intentar mover el peón a una posición inválida
        with self.assertRaises(InvalidMove):
            self.game.move(6, 0, 4, 1)  # Movimiento inválido para un peón

    def test_empty_position_move(self):
        # Intentar mover desde una posición vacía
        with self.assertRaises(EmptyPosition):
            self.game.move(5, 1, 4, 1)  # No hay ninguna pieza en (5, 1)

    def test_invalid_turn(self):
        # Coloca un peón blanco en la posición inicial y muévelo
        self.game.board.place_piece(Pawn("WHITE"), 6, 0)
        self.game.move(6, 0, 5, 0)  # Mueve el peón blanco

        # Intentar mover otra pieza blanca en el turno de las piezas negras
        self.game.board.place_piece(Pawn("WHITE"), 5, 1)
        with self.assertRaises(InvalidTurn):
            self.game.move(5, 1, 4, 1)  # Es turno de las piezas negras

    def test_pawn_promotion_to_queen(self):
        # Coloca un peón blanco en la fila 6 y promuévelo a reina
        self.game.board.place_piece(Pawn("WHITE"), 6, 0)
        self.game.move(6, 0, 0, 0, promotion_choice='queen')
        self.assertIsInstance(self.game.board.get_piece(0, 0), Queen)
        self.assertEqual(self.game.board.get_piece(0, 0).get_color(), "WHITE")

    def test_pawn_promotion_to_rook(self):
        # Coloca un peón blanco en la fila 6 y promuévelo a torre
        self.game.board.place_piece(Pawn("WHITE"), 6, 1)
        self.game.move(6, 1, 0, 1, promotion_choice='rook')
        self.assertIsInstance(self.game.board.get_piece(0, 1), Rook)
        self.assertEqual(self.game.board.get_piece(0, 1).get_color(), "WHITE")

    def test_pawn_promotion_to_bishop(self):
        # Coloca un peón blanco en la fila 6 y promuévelo a alfil
        self.game.board.place_piece(Pawn("WHITE"), 6, 2)
        self.game.move(6, 2, 0, 2, promotion_choice='bishop')
        self.assertIsInstance(self.game.board.get_piece(0, 2), Bishop)
        self.assertEqual(self.game.board.get_piece(0, 2).get_color(), "WHITE")

    def test_pawn_promotion_to_knight(self):
        # Coloca un peón blanco en la fila 6 y promuévelo a caballo
        self.game.board.place_piece(Pawn("WHITE"), 6, 3)
        self.game.move(6, 3, 0, 3, promotion_choice='knight')
        self.assertIsInstance(self.game.board.get_piece(0, 3), Knight)
        self.assertEqual(self.game.board.get_piece(0, 3).get_color(), "WHITE")

    def test_invalid_pawn_promotion_choice(self):
        # Coloca un peón blanco en la fila 6
        self.game.board.place_piece(Pawn("WHITE"), 6, 0)
        with self.assertRaises(ValueError):
            self.game.move(6, 0, 0, 0, promotion_choice='invalid_choice')

    def test_valid_attack_move(self):
        # Coloca un peón blanco y una pieza negra para verificar un ataque válido
        self.game.board.place_piece(Pawn("WHITE"), 6, 0)
        self.game.board.place_piece(Pawn("BLACK"), 5, 1)
        self.game.move(6, 0, 5, 1)  # El peón blanco captura al peón negro
        self.assertIsInstance(self.game.board.get_piece(5, 1), Pawn)
        self.assertEqual(self.game.board.get_piece(5, 1).get_color(), "WHITE")

    def test_invalid_attack_move(self):
        # Coloca un peón blanco y una pieza amiga en la posición de ataque
        self.game.board.place_piece(Pawn("WHITE"), 6, 0)
        self.game.board.place_piece(Pawn("WHITE"), 5, 1)
        with self.assertRaises(InvalidMove):
            self.game.move(6, 0, 5, 1)  # Movimiento inválido, no se puede atacar a una pieza amiga

if __name__ == '__main__':
    unittest.main()
