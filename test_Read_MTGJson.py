import pytest
from ReadMTGJson import ReadCards


@pytest.fixture
def test_read_card():
    return ReadCards()


