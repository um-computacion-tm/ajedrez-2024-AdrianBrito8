# Changelog

##[2024-08-17]

### Added
- Implemented `Board` 
- Created `Rook` 
- Added `Piece`
- Added `Pawn`
- Added `Cli`
- Added `Chess`

### Improved
- Enhanced `Piece` class to use protected `__color__` attribute. Added methods for color and string representation.

### Tests
- Added `test_piece.py` to verify color and string representation for `Piece`.
- Added `test_rook.py` to test color and string representation for `Rook`.
- Added `test_board.py`to test initial board setup and `get_piece` functionality.

 ##[2024-08-18]

 ## Improved
 -Added boundary checks in the `get_piece` and `move_piece` methods to ensure moves are within board limits.

 ## Tests
 - Tests the movement of a piece on the board and verifies that it was performed correctly.
 - Ensures that an `IndexError` is raised when trying to move a piece outside of the board's range.

##[2024-08-19]

## Improve
- Added `is_empty_position` methods to ensure operations are within board limits.

## Tests
- Tests the `is_empty_position` method to check for empty and occupied positions and verifies that an `IndexError` is raised for out-of-bounds positions.

##[2024-08-20]

## Adedd
- Adedd valid_moves in rook

## Tests
- Tests the valid_moves in rook method in differents positions

##[2024-08-21]
## Adedd 
- A dedd is_opponent_piece in piece

## Tests
- Test test_is_opponent_piece_ method to chek if the other piece is from the oponnent

##[2024-08-22]
## Adedd
-Piece Class:
    Added move_to(new_position) method to update the internal position of a piece.
    Added set_position(position) and get_position() methods to manage the position attribute of a piece.
    Updated Piece class to include a __position__ attribute to store the piece's current position.

## Tests
- test_piece.py:
    Added tests for the new move_to() method to ensure that the piece's position is updated correctly.
    Added tests for set_position(position) and get_position() methods.

##[2024-08-23]
## Adedd
- Implemented capture method in the Piece class to handle the capturing of pieces.
- Added is_captured method to check if a piece has been captured.

## Tests
- Created a new test case in test_piece.py to verify the correct functionality of the capture method.

##[2024-08-24]
## Tests
- Validating the list of valid moves from edge positions on the board.
- Validating the list of valid moves from a central position on the board.

##[2024-08-25]

### Added
- Added a `can_attack` method to the `Rook` class to check if the rook can attack a piece at a given position.
- Created unit tests for the `can_attack` method in `test_rook.py`.

##[2024-08-26]

 ## Added:
 - Pawn: 
    -valid_moves: Returns a list of valid moves for the pawn based on its current position and color.
    -move: Updates the pawn's status to indicate that it has moved, which affects its ability to make a double move on its first move.

 ## Tests
 - Tests Pawn:
    -test_pawn_valid_moves: Verifies the valid moves for a pawn from its initial position.

##[2024-08-27]

## Added:
- Board:
    -Added the place_piece(piece, row, col) method to allow placing a piece at a specific position on the board. 

- Pawn:
    -Updated valid_moves method

## Tests
- Added a test to verify that a pawn can capture enemy pieces with a diagonal move using the valid_moves method.


##[2024-08-31]

## Added:
- `Bishop` Class (`bishop.py`)
- `valid_moves(position)`: Calculates all valid diagonal moves from a given position.
  
## Tests
- `test_bishop_valid_moves_center`: Tests valid moves from a central position.
- `test_bishop_valid_moves_corner`: Tests valid moves from a corner position.

##[2024-09-01]

## Added:
- Queen` Class`
- Implemented the `Queen` piece by combining `Rook` and `Bishop` movements with methods

## Tests
- `test_queen_valid_moves_center`: Tests valid moves from a central position.
- `test_queen_valid_moves_corner`: Tests valid moves from a corner position.
- `test_queen_color`: Tests correct color assignment.

##[2024-09-02]

## Added:
- Class `Knight`
- Implemented movements methods.

## Tests:
- `test_knight_valid_moves` Tests valid moves 
- `test_knight_color` Tests correct color assigment

##[2024-09-03]

## Imrpoved
-`Knight` Class: Adjusted the implementations of the __str__ and can_attack methods

## Tests
-`test_knight_str`: Verified and corrected the string representation of the Knight to return the expected value "N(W)" for a white knight and "N(B)" for a black knight.
-`test_knight_can_attack`: Corrected the conditions for the can_attack method, ensuring that the knight can only attack enemy pieces and not friendly pieces or empty positions.

##[2024-09-04]

## Added:
- Class `King`
- Implemented `valid_moves` and `can_attack`

## Tests
- `test_king_color`: Ensures the King has the correct color (Black or White).
- `test_king_valid_moves`: Verifies the valid moves for the King from a central position on the board.
- `test_king_can_attack`: Confirms that the King can attack adjacent enemy pieces but not friendly ones.

##[2024-09-05]

## Added:
- `Board` Class: Implemented is_enemy_piece method to check if a piece at a target position belongs to the opposing player. (Second commit fixed)
- `Bishop` Class: can_attack method now properly checks if the target position contains an enemy piece using the is_enemy_piece method from the Board class.

## Tests
- Updated tests for the `Bishop` class to ensure can_attack correctly verifies if a piece can capture an enemy piece.

##[2024-09-06]

## Added:
- can_attack method for `Queen` class to check if the queen can attack an enemy piece.

## Tests
-Tests for Queen's can_attack functionality.

##[2024-09-08]

## Added:
- `Pawn` Class: Implemented a new method to promove pawn.
- `Board` Class: Implemented set_piece.

## Tests
- Tested in `test_pawn` all pieces to promote.

##[2024-09-09]
 
## Added:
- EXceptions

## Tried
- Tried to implement chess but didnt work

##[2024-09-10]

## Tried
- Second try on chess, i think i made a progress

##[2024-09-13]

## Improved:
- Chess finally works

## Test
- Tests `CHess`: improved `test_invalid_move` and finally works

##[2024-09-15]

## Improved:
- Starting de implementation of `Cli`

##[2024-09-16]

## Improved:
- Implemented all pieces on the `Board` (maybe i had to do it earlier)

##[2024-09-17]

## Added:
- Added `test_invalid_moves` in `Bishop`, `Rook`, `Knight`

##[2024-09-18]

## Improve:
- Imrpoved `can_attack` in `Bishop`

##[2024-09-19]

## Improve:
- Imrpoved `can_attack` in `Rook`

##[2024-09-20]

## Added:
- Added `cannot_attack` tests in `Rook` and `Bishop`

##[2024-09-21]
## Added:
- Added `cannot_attack` tests in `Knight`

##[2024-09-22]
## Added:
- Added `can_attack` in `Pawn`
- Added logic to decompose target_position into row and col.

## Tests:
- Tests added for `can_attack` and some extra cases

##[2024-09-23]
## Improve:
-Imrpoved `can_attack` and `cannot_attack` tests in `King`

##[2024-09-24]
## Added:
- Added `invalid_moves` in `King`

##[2024-09-27]
## Added:
- Added `invalid_moves` in `Queen`

##[2024-09-29]
## Improve:
- `Board` Class Improvements:
- Enhanced move_piece Validation: Added comprehensive turn validation to ensure that moves alternate correctly between black and white pieces.
- Enhanced Exceptions: Introduced the InvalidTurn exception to indicate when a move is attempted out of turn.
- Bug Fix: Fixed a bug where moves to positions occupied by enemy pieces were incorrectly flagged as invalid. Now, capturing enemy pieces is allowed as per chess rules.
- Validation Refinements: Improved boundary checks and validation in the move_piece method to ensure proper handling of all movement rules.

##[2024-09-30]
## Added:
- Added a `remove_piece` method to the `Board` class to remove a piece from the board at a specified position.

## Improve:
- Modified the `promote_pawn` method in the `Chess` class to use the remove_piece method to remove the pawn before promoting it.
- Modified the `is_valid_move` method in the `Chess` class to allow pawns to move to the opposite side of the board.
- Modified the `move` method in the `Chess` class to check if the pawn has reached the opposite side of the board before promoting it.
- Modified the `test_invalid_pawn_promotion_choice` test to expect a ValueError exception instead of an InvalidMove exception.
- Modified the `move` method in the `Chess` class to check if the pawn has reached the opposite side of the board before checking the promotion choice.

##[2024-10-01]
## Improve:
- Simplified the `show_board` method in the `Board` class to represent pieces with standard chess notation:

    White pieces are represented with uppercase letters (R, N, B, Q, K, P).
    Black pieces are represented with lowercase letters (r, n, b, q, k, p).

- Improved user input validation in the `CLI` to guide players when incorrect formats are entered.
- Enhanced `CLI` display for better readability of the current game state.

##[2024-10-02]
## Improve:
- Improved `str` in all pieces.
- Corrected piece representation in tests to match current implementation.
- Updated `test_initial_board` and `test_board_after_move` tests to expect uppercase letters for white pieces and lowercase letters for black pieces.


##[2024-10-03]
## Added:
- Added `get_king_position` method

## Tests:
- Added test case for `get_king_position` method to ensure it returns None when the king is not on the board.

##[2024-10-04]
## Added:
- A new helper method, `is_in_check` was added.
 This method checks whether a given position would be under attack by any enemy piece, thereby preventing the king from moving into such a position.

## Improve:
- The `valid_moves` method has been modified to include an optional check_check parameter.
 This allows checking whether the move puts the king in check before adding it to the list of valid moves.

 ##[2024-10-06]
 ## Added:
 - Added test case for `test_knight_can_jump_over_pieces` to ensure the knight can jump over pieces on the board.
- Added `move` method to the `Knight` class to handle movement of the knight on the board.

 ##[2024-10-07]
 ## Added:
 - Added a `move` method to handle the Queen's movement on the board: the method checks if the new position is valid using valid_moves. If valid, it moves the Queen to the new position and updates the board.

## Tests:
- Added a new test `test_queen_move` to verify that the Queen can move like a Rook and Bishop. The test ensures the Queen moves correctly on the board, updating its position.

##[2024-10-08]
## Added:
- Added the `move` method to the `King` class, allowing the king to move to a new valid position on the board.

## Tests:
- Added a new test `test_king_move` to verify that the king can move correctly to a valid square.

##[2024-10-09]
## Added:
- Added a new method `move` to update the pawn's position

## Tests:
- Added test `test_pawn_move` to verify the correct behavior of the move and ensures the pawn's position is updated correctly after the move

##[2024-10-10]
## Added:
- Added a new method `move` to update the rook's position

## Tests:
- Added test `test_rook_move` to verify the correct behavior of the move and ensures the rook's position is updated correctly after the move

##[2024-10-11]
## Added:
- Added a new method `move` to update the bishop's position

## Tests:
- Added test `test_bishop_move` to verify the correct behavior of the move and ensures the bishop's position is updated correctly after the move