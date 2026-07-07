import pytest

from references.ch07 import p0751_unit_descriptor as unit_mod


def test_measured_descriptor_accepts_matching_dimension() -> None:
    # Arrange
    length = (1, 0, 0)

    class Particle:
        position = unit_mod.Measured(length)

    particle = Particle()

    # Act
    particle.position = unit_mod.Quantity(3.0, length)

    # Assert
    assert particle.position == unit_mod.Quantity(3.0, length)
    # pyrefly: ignore [missing-attribute]
    assert particle.position.value == 3.0  # ty:ignore[unresolved-attribute]


def test_measured_descriptor_rejects_wrong_dimension() -> None:
    # Arrange
    length = (1, 0, 0)
    velocity = (1, 0, -1)

    class Particle:
        position = unit_mod.Measured(length)

    particle = Particle()

    # Act
    with pytest.raises(TypeError) as exc_info:
        particle.position = unit_mod.Quantity(2.0, velocity)

    # Assert
    assert str(exc_info.value) == "position expects dimension (1, 0, 0), got (1, 0, -1)"


def test_measured_descriptor_rejects_non_quantity_value() -> None:
    # Arrange
    length = (1, 0, 0)

    class Particle:
        position = unit_mod.Measured(length)

    particle = Particle()

    # Act
    with pytest.raises(TypeError) as exc_info:
        # pyrefly: ignore [bad-argument-type]
        particle.position = "not a quantity"  # ty:ignore[invalid-assignment]

    # Assert
    assert str(exc_info.value) == "position expects a Quantity, got str"


def test_measured_descriptor_reports_unset_attribute_as_missing() -> None:
    # Arrange
    length = (1, 0, 0)

    class Particle:
        position = unit_mod.Measured(length)

    particle = Particle()

    # Act
    actual = hasattr(particle, "position")

    # Assert
    assert actual is False


def test_quantity_equality_requires_matching_dimension() -> None:
    # Arrange
    length = (1, 0, 0)
    velocity = (1, 0, -1)

    # Act
    actual = unit_mod.Quantity(3.0, length) == unit_mod.Quantity(3.0, velocity)

    # Assert
    assert actual is False
