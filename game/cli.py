# cli.py
from game.chess import Chess
from game.exceptions import InvalidMove, InvalidTurn, EmptyPosition

def main():
    chess = Chess()
    while True:
        play(chess)

def play(chess):
    try:
        # print(chess.show_board())
        print("Turn:", chess.current_turn)
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To row: "))
        to_col = int(input("To col: "))
        promotion_choice = input("Promotion choice (queen/rook/bishop/knight, leave empty if not applicable): ").strip().lower()
        chess.move(from_row, from_col, to_row, to_col, promotion_choice if promotion_choice else None)
    except EmptyPosition:
        print("Error: The starting position is empty.")
    except InvalidTurn:
        print("Error: It's not your turn to move this piece.")
    except InvalidMove:
        print("Error: Invalid move for this piece.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    main()
