import pytest

from references.ch09 import p0900_csv_amounts as csv_mod


def test_sum_csv_amounts_sums_duplicate_names() -> None:
    # Arrange
    text = "name,amount\nspam,2\nspam,3\neggs,1\n"

    # Act
    actual = csv_mod.sum_csv_amounts(text)

    # Assert
    assert actual == {"spam": 5, "eggs": 1}


@pytest.mark.parametrize("text", ["", "   \n"])
def test_sum_csv_amounts_returns_empty_dict_for_blank_text(text: str) -> None:
    # Arrange

    # Act
    actual = csv_mod.sum_csv_amounts(text)

    # Assert
    assert actual == {}


def test_sum_csv_amounts_accepts_quoted_commas() -> None:
    # Arrange
    text = 'name,amount\n"green, tea",4\n'

    # Act
    actual = csv_mod.sum_csv_amounts(text)

    # Assert
    assert actual == {"green, tea": 4}


@pytest.mark.parametrize("text", ["name\nspam\n", "amount\n1\n"])
def test_sum_csv_amounts_rejects_missing_required_columns(text: str) -> None:
    # Arrange

    # Act
    with pytest.raises(ValueError) as exc_info:
        csv_mod.sum_csv_amounts(text)

    # Assert
    assert str(exc_info.value) == "CSV must contain name and amount columns"
