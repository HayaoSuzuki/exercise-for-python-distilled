import math

import pytest
from hypothesis import given
from hypothesis import strategies as st

from references.ch01 import p0104_text_entropy as entropy_mod
from tests._helpers import FAST


@pytest.mark.parametrize(("text", "expected"), [("", 0.0), ("aaaa", 0.0), ("abab", 1.0)])
def test_entropy_returns_exact_values_for_simple_text(text: str, expected: float) -> None:
    # Arrange

    # Act
    actual = entropy_mod.entropy(text)

    # Assert
    assert actual == expected


@pytest.mark.parametrize(("text", "expected"), [("abcabcabc", 1.584963), ("aab", 0.918296)])
def test_entropy_matches_known_rounded_values(text: str, expected: float) -> None:
    # Arrange

    # Act
    actual = round(entropy_mod.entropy(text), 6)

    # Assert
    assert actual == expected


@FAST
@given(st.text(alphabet=st.characters(max_codepoint=0x7F), max_size=40))
def test_entropy_does_not_exceed_uniform_distribution_bound(text: str) -> None:
    # Arrange
    expected_upper_bound = 0.0 if not text else math.log2(len(set(text))) + 1e-12

    # Act
    actual = entropy_mod.entropy(text)

    # Assert
    assert actual <= expected_upper_bound

