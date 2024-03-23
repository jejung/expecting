from datetime import datetime

import pytest

import expecting.list


@pytest.mark.parametrize(
    'current,expected',
    (
        ([], []),
        (tuple(), tuple()),
        ([1], [1]),
        ((1,), (1,)),
        ([1, 2], [1]),
        ([1, 2], [2]),
        ((1, 2), (1,)),
        ((1, 2), (2,)),
        (['asa', 2, True, object()], [True, 2]),
        (('asa', 2, True, object()), (True, 2)),
        (['asa', 2, True, object()], (True, 2)),
        (('asa', 2, True, object()), [True, 2]),
        ([True, 'asa', 2, 2, True, object()], [True, 2]),
        (('asa', True, 2, 2, True, object()), (True, 2)),
        ([True, 'asa', 2, 2, True, object()], (True, 2)),
        (('asa', True, 2, 2, True, object()), [True, 2]),
        ((datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),), (expecting.string.datetime.iso8601_full(),)),
    ),
)
def test_list_containing_matches(current, expected) -> None:
    assert current == expecting.list.containing(expected)


@pytest.mark.parametrize(
    'current,expected',
    (
        ([], [1]),
        (tuple(), (1,)),
        ([1], [2]),
        ((1,), (2,)),
        (['asa', 2, True, object()], [False, 1]),
        (('asa', 2, True, object()), (False, 1)),
        (['asa', 2, True, object()], (False, 1)),
        (('asa', 2, True, object()), [False, 1]),
        (['asa', 2, True, object()], [True, 1]),
        (('asa', 2, True, object()), (True, 1)),
        (['asa', 2, True, object()], (True, 1)),
        (('asa', 2, True, object()), [True, 1]),
        (['asa', 2, True, object()], [False, 2]),
        (('asa', 2, True, object()), (False, 2)),
        (['asa', 2, True, object()], (False, 2)),
        (('asa', 2, True, object()), [False, 2]),
        ((datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),), (expecting.string.datetime.iso8601_day(),)),
    ),
)
def test_list_containing_does_not_match(current, expected) -> None:
    assert current != expecting.list.containing(expected)


@pytest.mark.parametrize(
    'current,expected',
    (
        ([], []),
        (tuple(), tuple()),
        ([1], [1]),
        ((1,), (1,)),
        ([1, 2], [1, 2]),
        ((1, 2), (1, 2)),
        ([1, 2], [2, 1]),
        ((1, 2), (2, 1)),
        (['asa', 2, True], ['asa', True, 2]),
        (('asa', 2, True), ('asa', True, 2)),
        ((datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),), (expecting.string.datetime.iso8601_full(),)),
        ([datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')], [expecting.string.datetime.iso8601_full()]),
    ),
)
def test_list_unordered_matches(current, expected) -> None:
    assert current == expecting.list.unordered(expected)


@pytest.mark.parametrize(
    'current,expected',
    (
        ([], [1]),
        (tuple(), (1,)),
        ([1], [2]),
        ((1,), (2,)),
        ([1, 2], [2, 1, 3]),
        ((1, 2), (2, 1, 3)),
        (['asa', 2, False], ['asa', True, 2]),
        (('asa', 2, False), ('asa', True, 2)),
        (['asa', 2, True, 2], ['asa', True, 2]),
        (('asa', 2, True, 2), ('asa', True, 2)),
        ((datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),), (expecting.string.datetime.iso8601_day(),)),
        ([datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')], [expecting.string.datetime.iso8601_day()]),
    ),
)
def test_list_unordered_does_not_match(current, expected) -> None:
    assert current != expecting.list.unordered(expected)
