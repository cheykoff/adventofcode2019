import pytest
from day_01 import calculate_fuel, calculate_fuel_from_mass


@pytest.mark.parametrize("mass, fuel", [(12, 2), (14, 2), (1969, 654), (100756, 33583)])
def test_calculate_fuel_from_mass(mass, fuel):
    assert calculate_fuel_from_mass(mass) == fuel


def test_calculate_fuel():
    assert calculate_fuel(["12", "14", "1969", "100756"]) == 34241
