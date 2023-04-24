import pytest

from utils import dicts


@pytest.mark.parametrize('data, key, default, expected', [
    ({"vcs": "mercurial"}, "vcs", 'default', "mercurial"),
    ({"vcs": "boom"}, "vcs", 'default', "boom"),
    ({}, "vcs", 'default', 'default'),
    ({}, "vcs", 'it is default', 'it is default')
])
def test_get_val(data, key, default, expected):
    assert dicts.get_val(data, key, default) == expected
