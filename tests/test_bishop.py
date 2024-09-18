import unittest
from game.bishop import Bishop
from game.board import Board
from game.rook import Rook

class TestBishop(unittest.TestCase):
    def test_bishop_color(self):
        bishop_white = Bishop("WHITE")
        self.assertEqual(bishop_white.get_color(), "WHITE")
        
        bishop_black = Bishop("BLACK")
        self.assertEqual(bishop_black.get_color(), "BLACK")
    
    def test_bishop_str(self):
        bishop_white = Bishop("WHITE")
        self.assertEqual(str(bishop_white), "B(W)")
        
        bishop_black = Bishop("BLACK")
        self.assertEqual(str(bishop_black), "B(B)")
    
    def test_bishop_valid_moves_center(self):
        bishop = Bishop("WHITE")
        position = (4, 4)
        moves = bishop.valid_moves(position)
        
        expected_moves = [
            (3, 5), (2, 6), (1, 7),             # Up-Right
            (3, 3), (2, 2), (1, 1), (0, 0),     # Up-Left
            (5, 5), (6, 6), (7, 7),             # Down-Right
            (5, 3), (6, 2), (7, 1)              # Down-Left
        ]
        
        self.assertCountEqual(moves, expected_moves)
    
    def test_bishop_valid_moves_corner(self):
        bishop = Bishop("BLACK")
        position = (0, 0)
        moves = bishop.valid_moves(position)
        
        expected_moves = [
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)  # Down-Right
        ]
        
        self.assertCountEqual(moves, expected_moves)

    def test_bishop_invalid_moves(self):
        bishop = Bishop("WHITE", (4, 4))  # Posición central del tablero
        board = Board()

        # Movimientos que no son válidos para el alfil (no diagonales)
        invalid_moves = [(4, 5), (4, 6), (3, 4), (5, 4), (6, 4)]
    
        # Obtener los movimientos válidos
        valid_moves = bishop.valid_moves((4, 4), board)

        for move in invalid_moves:
            self.assertNotIn(move, valid_moves)


    def test_bishop_can_attack(self):
        board = Board()
        bishop = Bishop("WHITE", (4, 4))
        board.place_piece(bishop, 4, 4)

        # Caso 1: El alfil puede capturar una pieza enemiga en su diagonal
        enemy_piece = Rook("BLACK")
        board.place_piece(enemy_piece, 6, 6)  # Posición diagonal a (4, 4)
        self.assertTrue(bishop.can_attack((6, 6), board))  # Puede atacar

        # Caso 2: El alfil no puede atacar una pieza amiga
        friendly_piece = Rook("WHITE")
        board.place_piece(friendly_piece, 3, 3)  # Posición diagonal, pero misma color
        self.assertFalse(bishop.can_attack((3, 3), board))  # No debe atacar

        # Caso 3: El alfil no puede atacar una pieza fuera de su rango diagonal
        enemy_piece_far = Rook("BLACK")
        board.place_piece(enemy_piece_far, 4, 5)  # No está en una diagonal
        self.assertFalse(bishop.can_attack((4, 5), board))  # No puede atacar



if __name__ == '__main__':
    unittest.main()
