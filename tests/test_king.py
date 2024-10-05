import unittest
from game.king import King
from game.board import Board
from game.rook import Rook

class TestKing(unittest.TestCase):
    def test_king_color(self):
        king_white = King("WHITE")
        self.assertEqual(king_white.get_color(), "WHITE")
        
        king_black = King("BLACK")
        self.assertEqual(king_black.get_color(), "BLACK")

    def test_king_str(self):
        king_white = King("WHITE")
        self.assertEqual(str(king_white), "K")
        
        king_black = King("BLACK")
        self.assertEqual(str(king_black), "k")

    def test_king_valid_moves(self):
        king = King("BLACK")
        board = Board()
        moves = king.valid_moves((4, 4), board, check_check=False)

        expected_moves = [
            (5, 4), (3, 4), (4, 5), (4, 3),
            (5, 5), (3, 3), (5, 3), (3, 5)
        ]
        self.assertCountEqual(moves, expected_moves)

    def test_king_invalid_moves(self):
        board = Board()
        king = King("WHITE")
        board.place_piece(king, 4, 4)

        # Colocar una pieza amiga en una posición adyacente
        friendly_piece = Rook("WHITE")
        board.place_piece(friendly_piece, 5, 5)

        # Obtener los movimientos válidos del rey
        valid_moves = king.valid_moves((4, 4), board)

        # Movimientos inválidos que el rey no debe hacer
        invalid_moves = [
            (8, 8),  # Fuera del tablero
            (5, 5)   # Casilla ocupada por una pieza amiga
        ]

        # Asegurarse de que estos movimientos no estén entre los movimientos válidos
        for move in invalid_moves:
            self.assertNotIn(move, valid_moves)


    def test_king_can_attack(self):
        board = Board()
        king = King("WHITE")
        board.place_piece(king, 4, 4)

        # Test attack on an enemy piece (should attack)
        enemy_piece = Rook("BLACK")
        board.place_piece(enemy_piece, 5, 5)
        self.assertIn((5, 5), king.valid_moves((4, 4), board))

    def test_king_cannot_attack_friendly(self):
        board = Board()
        king = King("WHITE")
        board.place_piece(king, 4, 4)

        # Test that it cannot attack a friendly piece
        friendly_piece = Rook("WHITE")
        board.place_piece(friendly_piece, 3, 3)
        self.assertNotIn((3, 3), king.valid_moves((4, 4), board))

    def test_king_cannot_attack_empty(self):
        board = Board()
        king = King("WHITE")
        board.place_piece(king, 4, 4)

        self.assertIn((5, 5), king.valid_moves((4, 4), board))

    def test_king_in_check(self):
        board = Board()
        king = King("WHITE")
        board.place_piece(king, 4, 4)

        # Colocar una torre negra que amenace al rey
        rook = Rook("BLACK")
        board.place_piece(rook, 4, 7)

        # Verificar que el rey está en jaque
        self.assertTrue(king.is_in_check((4, 4), board))

    def test_king_valid_moves_avoid_check(self):
        board = Board()
        king = King("WHITE")
        board.place_piece(king, 4, 4)

        # Colocar una torre negra que amenace una de las posiciones válidas del rey
        rook = Rook("BLACK")
        board.place_piece(rook, 4, 6)

        # Verificar los movimientos válidos del rey (no debería incluir (4, 5))
        valid_moves = king.valid_moves((4, 4), board)
        self.assertNotIn((4, 5), valid_moves)

if __name__ == '__main__':
    unittest.main()
