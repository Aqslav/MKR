from IO_helper import IO_helper
from population import Population
import pytest


@pytest.mark.parametrize("data, expected", [
    ([Population("CountryA", 2020, 1000000)], "CountryA,2020,1000000"),
    ([Population("CountryB", 2019, 500000), Population("CountryC", 2021, 200000)], 
     "CountryB,2019,500000\nCountryC,2021,200000"),
    ([], "")
])
def test_stringify(data, expected):
    assert IO_helper.stringify(data) == expected


@pytest.mark.parametrize("input, expected", [
    ("CountryA,2020,1000000", Population("CountryA", 2020, 1000000)),
    ("CountryB,2019,500000", Population("CountryB", 2019, 500000)),
    ("CountryC,2021,200000", Population("CountryC", 2021, 200000))
])
def test_parse(input, expected):
    parsed = IO_helper.parse(input)
    assert parsed.country == expected.country
    assert parsed.year == expected.year
    assert parsed.population == expected.population
