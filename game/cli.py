from game.chess import Chess
from game.pawn import Pawn
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition

def main():
    print("Bienvenido al juego de ajedrez CLI.")
    chess = Chess()
    move_history = []  # To store the history of moves

    while not chess.is_game_over:
        play(chess, move_history)

    print_game_result(chess)

def play(chess, move_history):
    print(chess.board.show_board())
    print("Turno:", chess.current_turn)

    move = input("Ingrese su movimiento (ej: e2-e4), 'draw' para ofrecer tablas, o 'salir' para terminar: ").strip().lower()
    
    if move == 'salir':
        print("Juego terminado por el jugador.")
        chess.is_game_over = True
        return

    if move == 'draw':
        handle_draw_offer(chess)
        return

    try:
        from_pos, to_pos = parse_move(move)
        promotion_choice = check_pawn_promotion(chess, from_pos, to_pos)
        
        chess.move(from_pos[0], from_pos[1], to_pos[0], to_pos[1], promotion_choice)
        move_history.append(move)
        
    except (EmptyPosition, InvalidTurn, InvalidMove, ValueError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def handle_draw_offer(chess):
    if offer_draw(chess):
        chess.is_game_over = True
    else:
        print("Draw offer declined. The game continues.")

def check_pawn_promotion(chess, from_pos, to_pos):
    moving_piece = chess.board.get_piece(from_pos[0], from_pos[1])
    if isinstance(moving_piece, Pawn):
        if (moving_piece.get_color() == "WHITE" and to_pos[0] == 0) or \
           (moving_piece.get_color() == "BLACK" and to_pos[0] == 7):
            return input("Promoción (queen/rook/bishop/knight): ").strip().lower()
    return None

def offer_draw(chess):
    other_player = "BLACK" if chess.current_turn == "WHITE" else "WHITE"
    accept = input(f"{other_player}, do you accept the draw offer? (y/n): ").strip().lower()
    if accept == 'y':
        chess.agree_to_draw()
        return True
    return False

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

def print_game_result(chess):
    print("¡El juego ha terminado!")
    if chess.winner == "DRAW":
        print("El juego ha terminado en empate.")
    elif chess.winner:
        print(f"¡{chess.winner} ha ganado el juego!")
    else:
        print("El juego ha terminado sin un ganador claro.")

if __name__ == '__main__':
    main()