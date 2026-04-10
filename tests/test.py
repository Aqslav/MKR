from IO_helper import IO_helper
from population import Population
from get_population import PopulationDataManager
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


@pytest.fixture
def sample_data():
    return [
        Population("CountryA", 2020, 1000000),
        Population("CountryB", 2019, 500000),
        Population("CountryC", 2021, 200000)
    ]


def test_sort_by_year(sample_data):
    sorted_data = PopulationDataManager.sort_by_year(sample_data)
    assert sorted_data[0].year == 2019
    assert sorted_data[1].year == 2020
    assert sorted_data[2].year == 2021


def test_get_difference(sample_data):
    differences = PopulationDataManager.get_difference(sample_data)
    assert len(differences) == 2
    assert differences[0].population == 1000000 - 500000
    assert differences[1].population == 200000 - 1000000
