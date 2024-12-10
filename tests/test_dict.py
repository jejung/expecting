import pytest

import expecting.dict
import expecting.list


@pytest.mark.parametrize(
    'current,expected',
    (
        ({}, {}),
        ({'a': 1}, {}),
        ({'a': 1}, {'a': 1}),
        ({'a': 1, 1: object()}, {'a': 1}),
        ({'a': 1, 1: 2}, {1: 2}),
        ({'a': [1, 2, 3]}, {'a': expecting.list.containing([1])}),
    )
)
def test_dict_containing_matches(current, expected) -> None:
    assert current == expecting.dict.containing(expected)


@pytest.mark.parametrize(
    'current,expected',
    (
        (None, {}),
        (object(), {}),
        ({'a': 1}, {'a': 2}),
        ({'a': 1}, {'b': 1}),
        ({'a': 1, 'b': 1}, {'a': 1, 'b': 1, 'c': 1}),
        ({'a': [1, 2, 3]}, {'a': expecting.list.containing([4])}),
    )
)
def test_dict_containing_not_matches(current, expected) -> None:
    assert current != expecting.dict.containing(expected)
