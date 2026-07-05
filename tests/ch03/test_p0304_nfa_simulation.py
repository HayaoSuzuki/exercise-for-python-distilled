import pytest

from references.ch03 import p0304_nfa_simulation as nfa_mod


@pytest.fixture
def second_from_last_one_delta() -> dict[tuple[str, str], set[str]]:
    return {
        ("q0", "0"): {"q0"},
        ("q0", "1"): {"q0", "q1"},
        ("q1", "0"): {"q2"},
        ("q1", "1"): {"q2"},
    }


@pytest.mark.parametrize(
    ("text", "expected"),
    [("0110", True), ("0101", False), ("10", True), ("1", False)],
)
def test_nfa_accepts_returns_expected_result_for_input_string(
    second_from_last_one_delta: dict[tuple[str, str], set[str]], text: str, expected: bool
) -> None:
    # Arrange

    # Act
    actual = nfa_mod.nfa_accepts(second_from_last_one_delta, "q0", {"q2"}, text)

    # Assert
    assert actual is expected


@pytest.mark.parametrize(("accepting", "expected"), [({"q0"}, True), ({"q2"}, False)])
def test_nfa_accepts_handles_empty_string(
    second_from_last_one_delta: dict[tuple[str, str], set[str]], accepting: set[str], expected: bool
) -> None:
    # Arrange

    # Act
    actual = nfa_mod.nfa_accepts(second_from_last_one_delta, "q0", accepting, "")

    # Assert
    assert actual is expected
