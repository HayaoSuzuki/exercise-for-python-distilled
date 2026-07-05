from references.ch04 import p0402_copy_board as copy_mod


def test_copy_board_returns_equal_board() -> None:
    # Arrange
    board = [["x", "."], [".", "o"]]

    # Act
    actual = copy_mod.copy_board(board)

    # Assert
    assert actual == [["x", "."], [".", "o"]]


def test_copy_board_returns_new_outer_list() -> None:
    # Arrange
    board = [["x"]]

    # Act
    actual = copy_mod.copy_board(board)

    # Assert
    assert actual is not board


def test_copy_board_returns_new_rows() -> None:
    # Arrange
    board = [["x"], ["o"]]

    # Act
    actual = copy_mod.copy_board(board)

    # Assert
    assert actual[0] is not board[0]


def test_copy_board_does_not_share_mutated_rows() -> None:
    # Arrange
    board = [["x", "."], [".", "o"]]
    copied = copy_mod.copy_board(board)

    # Act
    copied[0][0] = "o"

    # Assert
    assert board == [["x", "."], [".", "o"]]
