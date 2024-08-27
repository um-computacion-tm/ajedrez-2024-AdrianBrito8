import unittest
from game.pawn import Pawn
from game.board import Board
from game.rook import Rook

class TestPawn(unittest.TestCase):
    def test_pawn_valid_moves(self):
        board = Board()

        # Colocar peones blancos y negros en el tablero
        pawn_white = Pawn("WHITE")
        board.place_piece(pawn_white, 6, 4)

        pawn_black = Pawn("BLACK")
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
        pawn_white.move()
        pawn_black.move()

        # Posición tras un movimiento inicial
        board.move_piece(6, 4, 5, 4)  # Mover peón blanco
        board.move_piece(1, 4, 2, 4)  # Mover peón negro

        moves = pawn_white.valid_moves((5, 4), board)
        expected_moves = [(4, 4)]  # Solo un movimiento hacia adelante disponible
        self.assertCountEqual(moves, expected_moves)

        moves = pawn_black.valid_moves((2, 4), board)
        expected_moves = [(3, 4)]  # Solo un movimiento hacia adelante disponible
        self.assertCountEqual(moves, expected_moves)

    def test_pawn_capture_diagonal(self):
        board = Board()
        
        pawn_white = Pawn("WHITE")
        board.place_piece(pawn_white, 6, 4)

        pawn_black_left = Rook("BLACK")
        board.place_piece(pawn_black_left, 5, 3)  # En diagonal a la izquierda

        pawn_black_right = Rook("BLACK")
        board.place_piece(pawn_black_right, 5, 5)  # En diagonal a la derecha

        moves = pawn_white.valid_moves((6, 4), board)
        expected_moves = [(5, 4), (4, 4), (5, 3), (5, 5)]  # Incluye capturas diagonales
        self.assertCountEqual(moves, expected_moves)

if __name__ == '__main__':
    unittest.main()

