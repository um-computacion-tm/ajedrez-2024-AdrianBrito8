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

