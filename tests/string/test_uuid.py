import uuid
from typing import Any

import pytest

import expecting.string


def test_uuid_v1_matches() -> None:
    assert str(uuid.uuid1()) == expecting.string.uuid.v1()


@pytest.mark.parametrize(
    'current',
    (
        None,
        '',
        10,
        uuid.uuid1(),
        uuid.uuid1().int,
        True,
        False,
        str(uuid.uuid3(uuid.uuid1(), 'wholesome')),
        str(uuid.uuid4()),
        str(uuid.uuid5(uuid.uuid1(), 'wholesome')),
    )
)
def test_uuid_v1_does_not_match(current: Any) -> None:
    assert current != expecting.string.uuid.v1()


def test_uuid_v3_matches() -> None:
    assert str(uuid.uuid3(uuid.uuid4(), 'bottles')) == expecting.string.uuid.v3()


@pytest.mark.parametrize(
    'current',
    (
        None,
        '',
        10,
        uuid.uuid3(uuid.uuid1(), 'false'),
        uuid.uuid3(uuid.uuid1(), 'false').int,
        True,
        False,
        str(uuid.uuid1()),
        str(uuid.uuid4()),
        str(uuid.uuid5(uuid.uuid1(), 'wholesome')),
    )
)
def test_uuid_v3_does_not_match(current: Any) -> None:
    assert current != expecting.string.uuid.v3()


def test_uuid_v4_matches() -> None:
    assert str(uuid.uuid4()) == expecting.string.uuid.v4()


@pytest.mark.parametrize(
    'current',
    (
        None,
        '',
        10,
        uuid.uuid4(),
        uuid.uuid4().int,
        True,
        False,
        str(uuid.uuid1()),
        str(uuid.uuid3(uuid.uuid1(), 'wholesome')),
        str(uuid.uuid5(uuid.uuid1(), 'wholesome')),
    )
)
def test_uuid_v4_does_not_match(current: Any) -> None:
    assert current != expecting.string.uuid.v4()


def test_uuid_v5_matches() -> None:
    assert str(uuid.uuid5(uuid.uuid4(), 'bottles')) == expecting.string.uuid.v5()


@pytest.mark.parametrize(
    'current',
    (
        None,
        '',
        10,
        uuid.uuid5(uuid.uuid1(), 'wholesome'),
        uuid.uuid5(uuid.uuid1(), 'wholesome').int,
        True,
        False,
        str(uuid.uuid1()),
        str(uuid.uuid3(uuid.uuid1(), 'wholesome')),
        str(uuid.uuid4()),
    )
)
def test_uuid_v5_does_not_match(current: Any) -> None:
    assert current != expecting.string.uuid.v5()


@pytest.mark.parametrize(
    'current',
    (
        str(uuid.uuid1()),
        str(uuid.uuid3(uuid.uuid4(), 'buggy')),
        str(uuid.uuid4()),
        str(uuid.uuid5(uuid.uuid1(), 'buggy')),
    )
)
def test_uuid_hex_matches(current: str) -> None:
    assert current == expecting.string.uuid.hex()


@pytest.mark.parametrize(
    'current',
    (
        None,
        '',
        10,
        uuid.uuid1(),
        uuid.uuid1().int,
        True,
        False,
    )
)
def test_uuid_hex_does_not_match(current: Any) -> None:
    assert current != expecting.string.uuid.hex()
