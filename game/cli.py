from game.chess import Chess
from game.pawn import Pawn
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition

def main():
    print("Bienvenido al juego de ajedrez CLI.")
    chess = Chess()
    move_history = []  # To store the history of moves

    while True:
        play(chess, move_history)

def play(chess, move_history):
    try:
        # Mostrar el tablero antes de cada movimiento
        print(chess.board.show_board())
        print("Turno:", chess.current_turn)

        # Check if the game is over before asking for input
        if chess.is_game_over:
            print("¡El juego ha terminado!")
            return

        # Pedir el movimiento en notación algebraica
        move = input("Ingrese su movimiento (ej: e2-e4) o 'salir' para terminar: ").strip().lower()
        if move == 'salir':
            print("Juego terminado.")
            exit()

        # Validar el movimiento
        from_pos, to_pos = parse_move(move)
        promotion_choice = None

        # Check if the moving piece is a pawn and if it reaches the promotion rank
        moving_piece = chess.board.get_piece(from_pos[0], from_pos[1])
        if isinstance(moving_piece, Pawn):
            if moving_piece.get_color() == "WHITE" and to_pos[0] == 0:
                promotion_choice = input("Promoción (queen/rook/bishop/knight): ").strip().lower()
            elif moving_piece.get_color() == "BLACK" and to_pos[0] == 7:
                promotion_choice = input("Promoción (queen/rook/bishop/knight): ").strip().lower()

        # Move the piece
        chess.move(from_pos[0], from_pos[1], to_pos[0], to_pos[1], promotion_choice)

        # Add the move to history
        move_history.append(move)

        # Check for game over after the move
        if chess.is_game_over:
            print("¡El juego ha terminado!")
            return

    except EmptyPosition:
        print("Error: La posición inicial está vacía.")
    except InvalidTurn:
        print("Error: No es tu turno para mover esta pieza.")
    except InvalidMove:
        print("Error: Movimiento inválido para esta pieza.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print("Error inesperado:", e)


def parse_move(move):
    try:
        from_pos, to_pos = move.split('-')
        from_row, from_col = parse_position(from_pos)
        to_row, to_col = parse_position(to_pos)
        return (from_row, from_col), (to_row, to_col)
    except (ValueError, IndexError):
        raise ValueError("Formato de movimiento inválido. Use 'e2-e4'.")

def parse_position(pos):
    col = ord(pos[0]) - ord('a')
    row = 8 - int(pos[1])
    return row, col

if __name__ == '__main__':
    main()