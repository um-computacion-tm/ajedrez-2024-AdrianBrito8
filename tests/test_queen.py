import unittest
from game.queen import Queen
from game.board import Board
from game.rook import Rook

class TestQueen(unittest.TestCase):
    def test_queen_color(self):
        queen_white = Queen("WHITE")
        self.assertEqual(queen_white.get_color(), "WHITE")
        
        queen_black = Queen("BLACK")
        self.assertEqual(queen_black.get_color(), "BLACK")
    
    def test_queen_str(self):
        queen_white = Queen("WHITE")
        self.assertEqual(str(queen_white), "Q")
        
        queen_black = Queen("BLACK")
        self.assertEqual(str(queen_black), "q")
    
    def test_queen_valid_moves_center(self):
        queen = Queen("WHITE")
        position = (4, 4)
        moves = queen.valid_moves(position)
        
        expected_moves = [
            # Horizontal moves
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7),
            # Vertical moves
            (0, 4), (1, 4), (2, 4), (3, 4), (5, 4), (6, 4), (7, 4),
            # Diagonal moves
            (3, 5), (2, 6), (1, 7), (3, 3), (2, 2), (1, 1), (0, 0),
            (5, 5), (6, 6), (7, 7), (5, 3), (6, 2), (7, 1)
        ]
        
        self.assertCountEqual(moves, expected_moves)
    
    def test_queen_valid_moves_corner(self):
        queen = Queen("BLACK")
        position = (0, 0)
        moves = queen.valid_moves(position)
        
        expected_moves = [
            # Horizontal moves
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
            # Vertical moves
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            # Diagonal moves
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)
        ]
        
        self.assertCountEqual(moves, expected_moves)

    def test_queen_invalid_moves(self):
        board = Board()
        queen = Queen("WHITE")
        position = (4, 4)

        # Colocar la reina en la posición (4, 4)
        board.place_piece(queen, *position)

        invalid_moves = [
            (4, 4),  # Misma posición
            (2, 5),  # Movimiento de "L" como un caballo
            (6, 3),  # Movimiento que no es recto ni diagonal
            (1, 6),  # Movimiento que no es recto ni diagonal
            (5, 1),  # Movimiento que no es recto ni diagonal
            (3, 7)   # Movimiento que no es recto ni diagonal
        ]

        # Movimientos válidos
        valid_moves = queen.valid_moves(position, board)

        for move in invalid_moves:
            self.assertNotIn(move, valid_moves)

    def test_queen_can_attack_enemy(self):
        board = Board()
        queen = Queen("WHITE")

        # Colocar la reina manualmente en el tablero
        board.place_piece(queen, 4, 4)
        queen.position = (4, 4) 

        enemy_piece = Rook("BLACK")
        board.place_piece(enemy_piece, 6, 6)

        self.assertTrue(queen.can_attack((6, 6), board))

    def test_queen_cannot_attack_friendly(self):
        board = Board()
        queen = Queen("WHITE")

        board.place_piece(queen, 4, 4)
        queen.position = (4, 4)

        friendly_piece = Rook("WHITE")
        board.place_piece(friendly_piece, 6, 6)

        self.assertFalse(queen.can_attack((6, 6), board))

    def test_queen_cannot_attack_empty(self):
        board = Board()
        queen = Queen("WHITE")

        board.place_piece(queen, 4, 4)
        queen.position = (4, 4)

        self.assertFalse(queen.can_attack((5, 5), board))

    def test_queen_move(self):
        board = Board()
        queen = Queen("WHITE", (4, 4))  # Establecer la posición inicial directamente
        board.place_piece(queen, 4, 4)

        # Verificar un movimiento válido
        valid_move = queen.move((6, 4), board)  # Movimiento estilo torre
        self.assertTrue(valid_move)
        self.assertEqual(queen.position, (6, 4))

        # Verificar un movimiento inválido
        invalid_move = queen.move((7, 7), board)  # Movimiento no permitido
        self.assertFalse(invalid_move)
        self.assertEqual(queen.position, (6, 4))  # No debe haber cambiado la posición

if __name__ == '__main__':
    unittest.main()
