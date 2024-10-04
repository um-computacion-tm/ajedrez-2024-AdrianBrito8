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

    def test_remove_piece(self):

        # Coloca un peón blanco en la posición (6, 0)
        self.board.place_piece(Pawn("WHITE"), 6, 0)
        self.assertIsInstance(self.board.get_piece(6, 0), Pawn)
        self.assertEqual(self.board.get_piece(6, 0).get_color(), "WHITE")

        # Elimina el peón blanco de la posición (6, 0)

        self.board.remove_piece(6, 0)
        self.assertIsNone(self.board.get_piece(6, 0))

        # Verifica que se lanza una excepción IndexError para posiciones fuera del tablero

        with self.assertRaises(IndexError):
            self.board.remove_piece(-1, 0)
        with self.assertRaises(IndexError):
            self.board.remove_piece(8, 0)
        with self.assertRaises(IndexError):
            self.board.remove_piece(0, 8)

class TestBoardShow(unittest.TestCase):

    def setUp(self):

        self.board = Board()

    def test_initial_board(self):
        expected_board = (
            "8 r n b q k b n r \n"
            "7 p p p p p p p p \n"
            "6 . . . . . . . . \n"
            "5 . . . . . . . . \n"
            "4 . . . . . . . . \n"
            "3 . . . . . . . . \n"
            "2 P P P P P P P P \n"
            "1 R N B Q K B N R \n"
            "  a b c d e f g h\n"
        )
        self.assertEqual(self.board.show_board(), expected_board)


    def test_board_after_move(self):

        # Mover un peón blanco de e2 a e4
        self.board.move_piece(6, 4, 4, 4)  # e2 -> e4

        expected_board_after_move = (
            "8 r n b q k b n r \n"
            "7 p p p p p p p p \n"
            "6 . . . . . . . . \n"
            "5 . . . . . . . . \n"
            "4 . . . . P . . . \n"
            "3 . . . . . . . . \n"
            "2 P P P P . P P P \n"
            "1 R N B Q K B N R \n"
            "  a b c d e f g h\n"
        )
        self.assertEqual(self.board.show_board(), expected_board_after_move)


    def test_get_king_position(self):
        # Crea un tablero vacío
        board = Board()

        # Elimina el rey negro de la posición (0, 4)

        board.remove_piece(0, 4)

        # Elimina el rey blanco de la posición (7, 4)

        board.remove_piece(7, 4)

        # Coloca un rey blanco en la posición (0, 0)

        king_white = King("WHITE")

        board.set_piece((0, 0), king_white)

        # Verifica que la posición del rey blanco sea (0, 0)

        self.assertEqual(board.get_king_position("WHITE"), (0, 0))

        # Coloca un rey negro en la posición (5, 5)

        king_black = King("BLACK")

        board.set_piece((5, 5), king_black)
        # Verifica que la posición del rey negro sea (5, 5)

        self.assertEqual(board.get_king_position("BLACK"), (5, 5))
        # Coloca un peón blanco en la posición (0, 0)

        pawn_white = Pawn("WHITE")

        board.set_piece((0, 0), pawn_white)

        # Verifica que la posición del rey blanco sea None

        self.assertIsNone(board.get_king_position("WHITE"))
        
        # Coloca un rey blanco en la posición (0, 0)
        king_white = King("WHITE")

        board.set_piece((0, 0), king_white)
        # Verifica que la posición del rey blanco sea (0, 0)
        self.assertEqual(board.get_king_position("WHITE"), (0, 0))

if __name__ == '__main__':
    unittest.main()
