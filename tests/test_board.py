import unittest
from game.board import Board
from game.rook import Rook
from game.pawn import Pawn
from game.knight import Knight
from game.bishop import Bishop
from game.queen import Queen
from game.king import King
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
    
    def test_board_initial_positions(self):
        # Verificar las torres negras
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertEqual(self.board.get_piece(0, 0).get_color(), "BLACK")
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertEqual(self.board.get_piece(0, 7).get_color(), "BLACK")

        # Verificar las torres blancas
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertEqual(self.board.get_piece(7, 0).get_color(), "WHITE")
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        self.assertEqual(self.board.get_piece(7, 7).get_color(), "WHITE")

        # Verificar los peones
        for col in range(8):
            self.assertIsInstance(self.board.get_piece(1, col), Pawn)
            self.assertEqual(self.board.get_piece(1, col).get_color(), "BLACK")
            self.assertIsInstance(self.board.get_piece(6, col), Pawn)
            self.assertEqual(self.board.get_piece(6, col).get_color(), "WHITE")

        # Verificar las demás piezas negras en la fila 0
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(0, 1), Knight)
        self.assertIsInstance(self.board.get_piece(0, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(0, 3), Queen)
        self.assertIsInstance(self.board.get_piece(0, 4), King)
        self.assertIsInstance(self.board.get_piece(0, 5), Bishop)
        self.assertIsInstance(self.board.get_piece(0, 6), Knight)
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)

        # Verificar las demás piezas blancas en la fila 7
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertIsInstance(self.board.get_piece(7, 1), Knight)
        self.assertIsInstance(self.board.get_piece(7, 2), Bishop)
        self.assertIsInstance(self.board.get_piece(7, 3), Queen)
        self.assertIsInstance(self.board.get_piece(7, 4), King)
        self.assertIsInstance(self.board.get_piece(7, 5), Bishop)
        self.assertIsInstance(self.board.get_piece(7, 6), Knight)
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)

    def test_get_piece_out_of_bounds(self):
        # Verifica que se lanza una excepción IndexError para posiciones fuera del tablero
        with self.assertRaises(IndexError):
            self.board.get_piece(-1, 0)

        with self.assertRaises(IndexError):
            self.board.get_piece(8, 0)

        with self.assertRaises(IndexError):
            self.board.get_piece(0, 8)

    def test_move_piece(self):
        # Mueve un peón blanco de (6, 0) a (4, 0)
        self.board.move_piece(6, 0, 4, 0)
        self.assertIsNone(self.board.get_piece(6, 0))
        self.assertIsInstance(self.board.get_piece(4, 0), Pawn)
        self.assertEqual(self.board.get_piece(4, 0).get_color(), "WHITE")

        # Turno de las negras: mover un peón negro de (1, 0) a (3, 0)
        self.board.move_piece(1, 0, 3, 0)
        self.assertIsNone(self.board.get_piece(1, 0))
        self.assertIsInstance(self.board.get_piece(3, 0), Pawn)
        self.assertEqual(self.board.get_piece(3, 0).get_color(), "BLACK")

        # Ahora es el turno de las blancas: intenta mover la torre blanca de (7, 7) a (5, 7)
        self.board.move_piece(7, 7, 5, 7)
        self.assertIsNone(self.board.get_piece(7, 7))
        self.assertIsInstance(self.board.get_piece(5, 7), Rook)
        self.assertEqual(self.board.get_piece(5, 7).get_color(), "WHITE")

        # Intentar un movimiento inválido para la torre negra (0, 7) a (1, 6) (debe fallar)
        with self.assertRaises(InvalidMove):
            self.board.move_piece(0, 7, 1, 6)


    def test_move_piece_out_of_bounds(self):
        # Verifica que se lanza una excepción IndexError para movimientos fuera del tablero
        with self.assertRaises(IndexError):
            self.board.move_piece(0, 0, 8, 8)

    def test_is_empty_position(self):
        # Verifica que las posiciones sin piezas son consideradas vacías
        self.assertTrue(self.board.is_empty_position(3, 3))
        self.assertTrue(self.board.is_empty_position(4, 4))

        # Verifica que las posiciones con piezas no son consideradas vacías
        self.assertFalse(self.board.is_empty_position(0, 0))
        self.assertFalse(self.board.is_empty_position(7, 7))

        # Verifica que se lanza una excepción IndexError para posiciones fuera del tablero
        with self.assertRaises(IndexError):
            self.board.is_empty_position(-1, 0)

        with self.assertRaises(IndexError):
            self.board.is_empty_position(8, 8)

if __name__ == '__main__':
    unittest.main()
