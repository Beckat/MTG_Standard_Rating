import pytest
from ReadMTGJson import ReadCards


@pytest.fixture
def test_read_card():
    return ReadCards()


def test_mana_cost(test_read_card):
    assert test_read_card.find_mana_cost_symbol("W", ['W']) == 'W', "Did not find W in ['W']"
    assert test_read_card.find_mana_cost_symbol("W", ['10', 'W', 'U']) == 'W', "Did not find W in ['10', 'W', 'U']"
    assert test_read_card.find_mana_cost_symbol("W", ['10', 'W', 'U', 'W']) == 'WW', "Did not find W in ['10', 'W', 'U', 'W']"
