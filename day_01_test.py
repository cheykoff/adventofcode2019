import pytest
from day_01 import calculate_fuel_from_mass


@pytest.mark.parametrize("mass, fuel", [(12, 2), (14, 2), (1969, 654), (100756, 33583)])
def test_calculate_fuel_from_mass(mass, fuel):
    assert calculate_fuel_from_mass(mass) == fuel


"""
def test_sum_fuel():
    fuel = sum_fuel(2, 2, 654, 33583)
    assert fuel == 34241
"""
