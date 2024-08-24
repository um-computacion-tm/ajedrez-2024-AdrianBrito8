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

##[2024-08-22]
## Adedd
- Implemented capture method in the Piece class to handle the capturing of pieces.
- Added is_captured method to check if a piece has been captured.

## Tests
- Created a new test case in test_piece.py to verify the correct functionality of the capture method.