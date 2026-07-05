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
    assert "expects dimension" in str(exc_info.value)
