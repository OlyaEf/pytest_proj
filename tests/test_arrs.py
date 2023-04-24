from utils import arrs
import pytest


@pytest.mark.parametrize('get, index, default, expected', [
    ([1, 2, 3], 1, 'default', 2),
    ([1, 2, 3], -1, 'default', 'default'),
    ([1, 2, 3], 0, 'default', 1)
])
def test_get(get, index, default, expected):
    assert arrs.get(get, index, default) == expected


def test_slice(slice_fixture):
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(slice_fixture, 1) == [2, 3]
    assert arrs.my_slice([], 1, 2) == []
    assert arrs.my_slice(slice_fixture, -1) == [3]
    assert arrs.my_slice(slice_fixture, -2) == [2, 3]
    assert arrs.my_slice(slice_fixture, -1, -3) == []
    assert arrs.my_slice(slice_fixture, -10) == [1, 2, 3]

