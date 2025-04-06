from typing import Any

import pytest

import expecting.number


@pytest.mark.parametrize(
    'left,right',
    (
        (1, 1),
        (2, 1),
        (1.0, 1),
        (2, 1.0),
        (2.0, 1.0),
        (2.0, 1),
    )
)
def test_number_ge_matches(left, right) -> None:
    assert left == expecting.number.ge(right)


@pytest.mark.parametrize(
    'left,right',
    (
        (None, 10),
        ('10', 10),
        ('av', 10),
        ('', 10),
        (object(), 10),
        (1, 2),
    )
)
def test_number_ge_does_not_match(left, right) -> None:
    assert left != expecting.number.ge(right)


@pytest.mark.parametrize(
    'left,right',
    (
        (1, 1),
        (1, 2),
        (1.0, 1),
        (1.0, 2),
        (1.0, 2.0),
        (1, 2.0),
    )
)
def test_number_le_matches(left, right) -> None:
    assert left == expecting.number.le(right)


@pytest.mark.parametrize(
    'left,right',
    (
        (None, 10),
        ('10', 10),
        ('av', 10),
        ('', 10),
        (object(), 10),
        (2, 1),
    )
)
def test_number_le_does_not_match(left, right) -> None:
    assert left != expecting.number.le(right)


@pytest.mark.parametrize(
    'left,right',
    (
        (2, 1),
        (2, 1.0),
        (2.0, 1.0),
        (2.0, 1),
    )
)
def test_number_gt_matches(left, right) -> None:
    assert left == expecting.number.gt(right)


@pytest.mark.parametrize(
    'left,right',
    (
        (None, 10),
        ('10', 10),
        ('av', 10),
        ('', 10),
        (object(), 10),
        (1, 1),
        (1, 2),
    )
)
def test_number_gt_does_not_match(left, right) -> None:
    assert left != expecting.number.gt(right)


@pytest.mark.parametrize(
    'left,right',
    (
        (1, 2),
        (1.0, 2),
        (1.0, 2.0),
        (1, 2.0),
    )
)
def test_number_lt_matches(left, right) -> None:
    assert left == expecting.number.lt(right)


@pytest.mark.parametrize(
    'left,right',
    (
        (None, 10),
        ('10', 10),
        ('av', 10),
        ('', 10),
        (object(), 10),
        (1, 1),
        (2, 1),
    )
)
def test_number_lt_does_not_match(left, right) -> None:
    assert left != expecting.number.lt(right)


@pytest.mark.parametrize(
    'left,right',
    (
        (1, 1),
        (1.0, 1.0),
        (1, 1.0),
        (1.0, 1),
    )
)
def test_number_eq_matches(left, right) -> None:
    assert left == expecting.number.eq(right)


@pytest.mark.parametrize(
    'left,right',
    (
        (None, 10),
        ('10', 10),
        ('av', 10),
        ('', 10),
        (object(), 10),
        (1, 2),
    )
)
def test_number_eq_does_not_match(left, right) -> None:
    assert left != expecting.number.eq(right)


@pytest.mark.parametrize(
    'left,right',
    (
        (1, 2),
        (1.1, 1.0),
        (1, 1.1),
        (1.1, 1),
    )
)
def test_number_ne_matches(left, right) -> None:
    assert left == expecting.number.ne(right)


@pytest.mark.parametrize(
    'left,right',
    (
        (None, 10),
        ('10', 10),
        ('av', 10),
        ('', 10),
        (object(), 10),
        (1.0, 1.0),
        (1, 1.0),
        (1.0, 1),
    )
)
def test_number_ne_does_not_match(left, right) -> None:
    assert left != expecting.number.ne(right)



@pytest.mark.parametrize(
    'value',
    (
        0,
        1,
        -1,
        4.5,
        -4.5,
        '0',
        '1',
        '-1',
        '-4.5',
        '4.5',
        '-0',
        'inf',
        '-inf',
        True,
        False,
    )
)
def test_any_matches(value: Any) -> None:
    assert value == expecting.number.any()


@pytest.mark.parametrize(
    'value',
    (
        None,
        object(),
    )
)
def test_any_does_not_match(value: Any) -> None:
    assert value != expecting.number.any()
