import unittest
from game.knight import Knight
from game.board import Board
from game.rook import Rook

class TestKnight(unittest.TestCase):
    def test_knight_color(self):
        knight_white = Knight("WHITE")
        self.assertEqual(knight_white.get_color(), "WHITE")
        
        knight_black = Knight("BLACK")
        self.assertEqual(knight_black.get_color(), "BLACK")

    def test_knight_str(self):
        knight_white = Knight("WHITE")
        self.assertEqual(str(knight_white), "N(W)")
        
        knight_black = Knight("BLACK")
        self.assertEqual(str(knight_black), "N(B)")

    def test_knight_valid_moves(self):
        knight = Knight("BLACK", (4, 4))  # Set initial position
        board = Board()

        moves = knight.valid_moves((4, 4), board)
        expected_moves = [
            (6, 5), (6, 3), (2, 5), (2, 3),
            (5, 6), (5, 2), (3, 6), (3, 2)
        ]
        self.assertCountEqual(moves, expected_moves)

    def test_knight_invalid_moves(self):
        knight = Knight("BLACK", (4, 4))  # Posición inicial en el centro del tablero
        board = Board()

        # Movimientos que no son válidos para el caballo
        invalid_moves = [(4, 5), (3, 3), (5, 5), (6, 6), (2, 4)]
    
        # Obtener los movimientos válidos
        valid_moves = knight.valid_moves((4, 4), board)

        for move in invalid_moves:
            self.assertNotIn(move, valid_moves)


    def test_knight_can_attack(self):
        board = Board()
        knight = Knight("WHITE", (3, 3))  # Set initial position

        # Place the knight on the board
        board.place_piece(knight, 3, 3)

        # Test attack on empty square (should not attack)
        self.assertFalse(knight.can_attack((5, 4), board))

        # Test attack on an enemy piece (should attack)
        enemy_piece = Rook("BLACK")
        board.place_piece(enemy_piece, 5, 4)
        self.assertTrue(knight.can_attack((5, 4), board))

        # Test attack on a friendly piece (should not attack)
        friendly_piece = Rook("WHITE")
        board.place_piece(friendly_piece, 4, 5)
        self.assertFalse(knight.can_attack((4, 5), board))

if __name__ == '__main__':
    unittest.main()
