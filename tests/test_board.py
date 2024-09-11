import unittest
from game.board import Board
from game.rook import Rook

class TestBoard(unittest.TestCase):
    def test_board_initial_positions(self):
        board = Board()

        # Verifica que las torres negras están en las posiciones iniciales
        self.assertIsInstance(board.get_piece(0, 0), Rook)
        self.assertEqual(board.get_piece(0, 0).get_color(), "BLACK")
        
        self.assertIsInstance(board.get_piece(0, 7), Rook)
        self.assertEqual(board.get_piece(0, 7).get_color(), "BLACK")
        
        # Verifica que las torres blancas están en las posiciones iniciales
        self.assertIsInstance(board.get_piece(7, 0), Rook)
        self.assertEqual(board.get_piece(7, 0).get_color(), "WHITE")
        
        self.assertIsInstance(board.get_piece(7, 7), Rook)
        self.assertEqual(board.get_piece(7, 7).get_color(), "WHITE")

    def test_get_piece_out_of_bounds(self):
        board = Board()

        # Verifica que se lanza una excepción IndexError para posiciones fuera del tablero
        with self.assertRaises(IndexError):
            board.get_piece(-1, 0)

        with self.assertRaises(IndexError):
            board.get_piece(8, 0)

        with self.assertRaises(IndexError):
            board.get_piece(0, 8)

    def test_move_piece(self):
        board = Board()
        
        # Mueve la torre negra de (0, 0) a (0, 4)
        board.move_piece(0, 0, 0, 4)
        self.assertIsNone(board.get_piece(0, 0))
        self.assertIsInstance(board.get_piece(0, 4), Rook)
        self.assertEqual(board.get_piece(0, 4).get_color(), "BLACK")
        
        # Mueve la torre blanca de (7, 7) a (5, 7)
        board.move_piece(7, 7, 5, 7)
        self.assertIsNone(board.get_piece(7, 7))
        self.assertIsInstance(board.get_piece(5, 7), Rook)
        self.assertEqual(board.get_piece(5, 7).get_color(), "WHITE")

    def test_move_piece_out_of_bounds(self):
        board = Board()

        # Verifica que se lanza una excepción IndexError para movimientos fuera del tablero
        with self.assertRaises(IndexError):
            board.move_piece(0, 0, 8, 8)

    def test_is_empty_position(self):
        board = Board()

        # Verifica que las posiciones sin piezas son consideradas vacías
        self.assertTrue(board.is_empty_position(3, 3))
        self.assertTrue(board.is_empty_position(4, 4))

        # Verifica que las posiciones con piezas no son consideradas vacías
        self.assertFalse(board.is_empty_position(0, 0))
        self.assertFalse(board.is_empty_position(7, 7))

        # Verifica que se lanza una excepción IndexError para posiciones fuera del tablero
        with self.assertRaises(IndexError):
            board.is_empty_position(-1, 0)

        with self.assertRaises(IndexError):
            board.is_empty_position(8, 8)

if __name__ == '__main__':
    unittest.main()
