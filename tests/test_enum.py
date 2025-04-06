from enum import Enum
from typing import Type, Any

import pytest

import expecting.enum


class EnumForTests(str, Enum):
    VALUE1 = 'value1'
    VALUE2 = 'value2'
    VALUE3 = 'value3'


@pytest.mark.parametrize(
    'enum, value',
    (
        (EnumForTests, v.value)
        for v in EnumForTests
    )
)
def test_enum_any_value_of_matches(enum: Type[Enum], value: Any):
    assert value == expecting.enum.any_value_of(enum)


@pytest.mark.parametrize(
    'enum, value',
    (
        (EnumForTests, 'not a value'),
        (EnumForTests, None),
        (EnumForTests, 10),
        (EnumForTests, True),
        (EnumForTests, False),
    )
)
def test_enum_any_value_of_does_not_match(enum: Type[Enum], value: Any):
    assert value != expecting.enum.any_value_of(enum)

