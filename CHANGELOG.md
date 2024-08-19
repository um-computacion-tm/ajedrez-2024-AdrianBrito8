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

##[2024-08-17]

## Improve
- Added `is_empty_position` methods to ensure operations are within board limits.

## Tests
- Tests the `is_empty_position` method to check for empty and occupied positions and verifies that an `IndexError` is raised for out-of-bounds positions.
