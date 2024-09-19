import unittest
from game.rook import Rook
from game.board import Board
from game.piece import Piece

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

    def test_rook_valid_moves(self):
        rook = Rook("BLACK")
        
        # Position at (0, 0)
        moves = rook.valid_moves((0, 0))
        expected_moves = [(0, i) for i in range(1, 8)] + [(i, 0) for i in range(1, 8)]
        self.assertCountEqual(moves, expected_moves)
        
        # Position at (3, 3)
        moves = rook.valid_moves((3, 3))
        expected_moves = [(3, i) for i in range(8) if i != 3] + [(i, 3) for i in range(8) if i != 3]
        self.assertCountEqual(moves, expected_moves)

    def test_rook_invalid_moves(self):
        rook = Rook("BLACK")

        # Position at (0, 0) - Movimientos válidos: solo en la misma fila o columna
        invalid_moves = [(1, 1), (2, 2), (3, 3), (7, 7)]  # Movimientos diagonales inválidos
        valid_moves = rook.valid_moves((0, 0))

        for move in invalid_moves:
            self.assertNotIn(move, valid_moves)

    def test_rook_valid_moves_edge_case(self):
        rook = Rook("WHITE")
        
        moves = rook.valid_moves((7, 7))
        expected_moves = [(7, i) for i in range(7)] + [(i, 7) for i in range(7)]
        self.assertCountEqual(moves, expected_moves)

    def test_rook_valid_moves_central_position(self):
        rook = Rook("WHITE")
        
        # Position at (4, 4)
        moves = rook.valid_moves((4, 4))
        expected_moves = [(4, i) for i in range(8) if i != 4] + [(i, 4) for i in range(8) if i != 4]
        self.assertCountEqual(moves, expected_moves)

    def test_rook_can_attack(self):
        board = Board()

        # Colocar la torre en la posición (0, 0)
        rook = Rook("BLACK", (0, 0))
        board.place_piece(rook, 0, 0)

        # Añadir una pieza enemiga en la misma fila
        enemy_piece = Piece("WHITE")
        board.place_piece(enemy_piece, 0, 7)
        
        # Añadir una pieza enemiga en la misma columna
        enemy_piece_2 = Piece("WHITE")
        board.place_piece(enemy_piece_2, 7, 0)

        # Añadir una pieza aliada en la misma fila (no debería poder atacar)
        friendly_piece = Piece("BLACK")
        board.place_piece(friendly_piece, 0, 5)

        # Comprobamos que puede atacar a las piezas enemigas pero no a la pieza aliada
        self.assertTrue(rook.can_attack((0, 7), board))  # Puede capturar en la misma fila
        self.assertTrue(rook.can_attack((7, 0), board))  # Puede capturar en la misma columna
        self.assertFalse(rook.can_attack((0, 5), board))  # No puede atacar a su propio color
        self.assertFalse(rook.can_attack((7, 7), board))  # No puede atacar fuera de la fila/columna

if __name__ == '__main__':
    unittest.main()

