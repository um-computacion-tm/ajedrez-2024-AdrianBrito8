from game.chess import Chess
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition

def main():
    print("Bienvenido al juego de ajedrez CLI.")
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    try:
        # Mostrar el tablero antes de cada movimiento
        print(chess.board.show_board())
        print("Turno:", chess.current_turn)

        # Pedir las coordenadas desde y hacia en el formato de ajedrez
        from_pos = input("Desde (ej: e2) o 'salir' para terminar: ").strip().lower()
        if from_pos == 'salir':
            print("Juego terminado.")
            exit()

        to_pos = input("Hasta (ej: e4): ").strip().lower()

        # Validar entrada y convertirla a coordenadas
        if not valid_position(from_pos) or not valid_position(to_pos):
            print("Entrada inválida. Por favor, ingresa las coordenadas en el formato 'e2'.")
            return

        from_row, from_col = parse_position(from_pos)
        to_row, to_col = parse_position(to_pos)

        promotion_choice = input("Promoción (queen/rook/bishop/knight, dejar vacío si no aplica): ").strip().lower()
        chess.move(from_row, from_col, to_row, to_col, promotion_choice if promotion_choice else None)

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

def valid_position(pos):
    return len(pos) == 2 and pos[0] in "abcdefgh" and pos[1] in "12345678"

def parse_position(pos):
    col = ord(pos[0]) - ord('a')
    row = 8 - int(pos[1])
    return row, col

if __name__ == '__main__':
    main()
