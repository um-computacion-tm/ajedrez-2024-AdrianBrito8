import unittest
from game.pawn import Pawn
from game.queen import Queen
from game.rook import Rook
from game.bishop import Bishop
from game.knight import Knight
from game.board import Board


class TestPawn(unittest.TestCase):

    def test_pawn_str(self):
        pawn_white = Pawn("WHITE")
        self.assertEqual(str(pawn_white), "P")
        
        pawn_black = Pawn("BLACK")
        self.assertEqual(str(pawn_black), "p")

    def test_pawn_valid_moves(self):
        board = Board()

        # Colocar peones blancos y negros en el tablero
        pawn_white = Pawn("WHITE", (6, 4))
        board.place_piece(pawn_white, 6, 4)

        pawn_black = Pawn("BLACK", (1, 4))
        board.place_piece(pawn_black, 1, 4)

        # Blancas inicia
        moves = pawn_white.valid_moves((6, 4), board)
        expected_moves = [(5, 4), (4, 4)]  # Solo movimiento hacia adelante al inicio
        self.assertCountEqual(moves, expected_moves)

        # Negras inicia
        moves = pawn_black.valid_moves((1, 4), board)
        expected_moves = [(2, 4), (3, 4)]  # Solo movimiento hacia adelante al inicio
        self.assertCountEqual(moves, expected_moves)

        # Simular el primer movimiento de los peones
        board.move_piece(6, 4, 5, 4)
        pawn_white.move((5, 4))

        board.move_piece(1, 4, 2, 4)
        pawn_black.move((2, 4))

        # Posición tras un movimiento inicial
        moves = pawn_white.valid_moves((5, 4), board)
        expected_moves = [(4, 4)]  # Solo un movimiento hacia adelante disponible
        self.assertCountEqual(moves, expected_moves)

        moves = pawn_black.valid_moves((2, 4), board)
        expected_moves = [(3, 4)]  # Solo un movimiento hacia adelante disponible
        self.assertCountEqual(moves, expected_moves)

    def test_pawn_capture_diagonal(self):
        board = Board()
        
        pawn_white = Pawn("WHITE", (6, 4))
        board.place_piece(pawn_white, 6, 4)

        pawn_black_left = Pawn("BLACK", (5, 3))
        board.place_piece(pawn_black_left, 5, 3)  # En diagonal a la izquierda

        pawn_black_right = Pawn("BLACK", (5, 5))
        board.place_piece(pawn_black_right, 5, 5)  # En diagonal a la derecha

        moves = pawn_white.valid_moves((6, 4), board)
        expected_moves = [(5, 4), (4, 4), (5, 3), (5, 5)]  # Incluye capturas diagonales
        self.assertCountEqual(moves, expected_moves)

    def test_pawn_can_attack_enemy(self):
        board = Board()
        pawn_white = Pawn("WHITE", (6, 4))

        board.place_piece(pawn_white, 6, 4)

        enemy_piece = Rook("BLACK", (5, 3))
        board.place_piece(enemy_piece, 5, 3)  # En diagonal

        self.assertTrue(pawn_white.can_attack((5, 3), board))

    def test_pawn_cannot_attack_friendly(self):
        board = Board()
        pawn_white = Pawn("WHITE", (6, 4))

        board.place_piece(pawn_white, 6, 4)

        friendly_piece = Rook("WHITE", (5, 3))
        board.place_piece(friendly_piece, 5, 3)  # En diagonal

        self.assertFalse(pawn_white.can_attack((5, 3), board))

    def test_pawn_cannot_attack_empty(self):
        board = Board()
        pawn_white = Pawn("WHITE", (6, 4))

        board.place_piece(pawn_white, 6, 4)

        # No hay ninguna pieza en esta posición
        self.assertFalse(pawn_white.can_attack((5, 3), board))

    def test_pawn_move(self):
        pawn = Pawn("WHITE", (6, 4))
    
        # Asegurarse de que inicialmente el peón no se ha movido
        self.assertFalse(pawn.__moved__)
        self.assertEqual(pawn.position, (6, 4))
    
        # Mover el peón a una nueva posición
        pawn.move((5, 4))
    
        # Verificar que la posición se actualizó y que __moved__ ahora es True
        self.assertTrue(pawn.__moved__)
        self.assertEqual(pawn.position, (5, 4))

class TestPawnPromotion(unittest.TestCase):
    def test_pawn_promotion_to_queen(self):
        pawn = Pawn("WHITE")
        promoted_piece = pawn.promote("queen")
        self.assertIsInstance(promoted_piece, Queen)

    def test_pawn_promotion_to_rook(self):
        pawn = Pawn("WHITE")
        promoted_piece = pawn.promote("rook")
        self.assertIsInstance(promoted_piece, Rook)

    def test_pawn_promotion_to_bishop(self):
        pawn = Pawn("WHITE")
        promoted_piece = pawn.promote("bishop")
        self.assertIsInstance(promoted_piece, Bishop)

    def test_pawn_promotion_to_knight(self):
        pawn = Pawn("WHITE")
        promoted_piece = pawn.promote("knight")
        self.assertIsInstance(promoted_piece, Knight)

    def test_invalid_promotion_choice(self):
        pawn = Pawn("WHITE")
        with self.assertRaises(ValueError):
            pawn.promote("invalid_choice")


if __name__ == '__main__':
    unittest.main()
