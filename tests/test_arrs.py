import pytest
from utils import arrs

@pytest.fixture
def list_data():
    return [1, 2, 3]

def test_get(list_data):
    assert arrs.get(list_data, 1, "test") == 2
    assert arrs.get(list_data, -1, "test") == "test"
    assert arrs.get([], 0, "test") is None


def test_slice(list_data):
    assert arrs.my_slice(list_data, 1, 3) == [2, 3]
    assert arrs.my_slice(list_data, 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(list_data, -6) == [1, 2, 3]
    assert arrs.my_slice(list_data, -2) == [2, 3]
