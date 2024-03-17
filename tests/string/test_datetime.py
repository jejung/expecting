from datetime import datetime, timezone

import pytest

import expecting


@pytest.mark.parametrize(
    'datetime_str',
    (
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f+0000'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f+000000'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f+000000.000000'),
        datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        datetime.utcnow().astimezone(timezone.max).strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
        datetime.utcnow().astimezone(timezone.min).strftime('%Y-%m-%dT%H:%M:%S.%f%z'),
    )
)
def test_iso8601_full_matches(datetime_str: str):
    assert datetime_str == expecting.string.datetime.iso8601_full()


@pytest.mark.parametrize(
    'datetime_str',
    (
        '2023/10/11 13:01:10',
        '23-11-2023T10:01:22',
        '2023-15-15T10:01:22',
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        'not even a date',
        None,
        2023,
        datetime.now(),
    )
)
def test_iso8601_full_does_not_match(datetime_str: str):
    assert datetime_str != expecting.string.datetime.iso8601_full()


@pytest.mark.parametrize(
    'datetime_str',
    (
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
        datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f'),
        datetime.utcnow().astimezone(timezone.max).strftime('%Y-%m-%dT%H:%M:%S.%f'),
        datetime.utcnow().astimezone(timezone.min).strftime('%Y-%m-%dT%H:%M:%S.%f'),
    )
)
def test_iso8601_millisecond_matches(datetime_str: str):
    assert datetime_str == expecting.string.datetime.iso8601_millisecond()


@pytest.mark.parametrize(
    'datetime_str',
    (
        '2023/10/11 13:01:10',
        '23-11-2023T10:01:22',
        '2023-15-15T10:01:22',
        '2023-11-15T10:01:22.1000000.000000',
        '2023-11-15T10:01:22.000000.1000000',
        '2023-11-15T10:01:22.000000.-999999',
        '2023-11-15T10:01:22.-999999.999999',
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        datetime.utcnow().astimezone(timezone.min).strftime('%Y-%m-%dT%H:%M:%S.%f%Z'),
        datetime.utcnow().astimezone(timezone.max).strftime('%Y-%m-%dT%H:%M:%S.%f%Z'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f+00000.0000'),
        'not even a date',
        None,
        2023,
        datetime.now(),
    )
)
def test_iso8601_millisecond_does_not_match(datetime_str: str):
    assert datetime_str != expecting.string.datetime.iso8601_millisecond()


@pytest.mark.parametrize(
    'datetime_str',
    (
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S'),
        datetime.utcnow().astimezone(timezone.max).strftime('%Y-%m-%dT%H:%M:%S'),
        datetime.utcnow().astimezone(timezone.min).strftime('%Y-%m-%dT%H:%M:%S'),
    )
)
def test_iso8601_second_matches(datetime_str: str):
    assert datetime_str == expecting.string.datetime.iso8601_second()


@pytest.mark.parametrize(
    'datetime_str',
    (
        '2023/10/11 13:01:10',
        '23-11-2023T10:01:22',
        '2023-15-15T10:01:22',
        '2023-11-15T10:01:60',
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
        datetime.utcnow().astimezone(timezone.min).strftime('%Y-%m-%dT%H:%M:%S.%f%Z'),
        datetime.utcnow().astimezone(timezone.max).strftime('%Y-%m-%dT%H:%M:%S.%f%Z'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f+00000.0000'),
        'not even a date',
        None,
        2023,
        datetime.now(),
    )
)
def test_iso8601_second_does_not_match(datetime_str: str):
    assert datetime_str != expecting.string.datetime.iso8601_second()


@pytest.mark.parametrize(
    'datetime_str',
    (
        datetime.now().strftime('%Y-%m-%dT%H:%M'),
        datetime.utcnow().strftime('%Y-%m-%dT%H:%M'),
        datetime.utcnow().astimezone(timezone.max).strftime('%Y-%m-%dT%H:%M'),
        datetime.utcnow().astimezone(timezone.min).strftime('%Y-%m-%dT%H:%M'),
    )
)
def test_iso8601_minute_matches(datetime_str: str):
    assert datetime_str == expecting.string.datetime.iso8601_minute()


@pytest.mark.parametrize(
    'datetime_str',
    (
        '2023/10/11 13:01',
        '23-11-2023T10:01',
        '2023-15-15T10:01',
        '2023-11-15T10:60',
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
        datetime.utcnow().astimezone(timezone.min).strftime('%Y-%m-%dT%H:%M:%S.%f%Z'),
        datetime.utcnow().astimezone(timezone.max).strftime('%Y-%m-%dT%H:%M:%S.%f%Z'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f+00000.0000'),
        'not even a date',
        None,
        2023,
        datetime.now(),
    )
)
def test_iso8601_minute_does_not_match(datetime_str: str):
    assert datetime_str != expecting.string.datetime.iso8601_minute()


@pytest.mark.parametrize(
    'datetime_str',
    (
        datetime.now().strftime('%Y-%m-%dT%H'),
        datetime.utcnow().strftime('%Y-%m-%dT%H'),
        datetime.utcnow().astimezone(timezone.max).strftime('%Y-%m-%dT%H'),
        datetime.utcnow().astimezone(timezone.min).strftime('%Y-%m-%dT%H'),
    )
)
def test_iso8601_hour_matches(datetime_str: str):
    assert datetime_str == expecting.string.datetime.iso8601_hour()


@pytest.mark.parametrize(
    'datetime_str',
    (
        '2023/10/11 13',
        '23-11-2023T10',
        '2023-11-15T25',
        '2023-15-15T10',
        datetime.now().strftime('%Y-%m-%dT%H:%M'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
        datetime.utcnow().astimezone(timezone.min).strftime('%Y-%m-%dT%H:%M:%S.%f%Z'),
        datetime.utcnow().astimezone(timezone.max).strftime('%Y-%m-%dT%H:%M:%S.%f%Z'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f+00000.0000'),
        'not even a date',
        None,
        2023,
        datetime.now(),
    )
)
def test_iso8601_hour_does_not_match(datetime_str: str):
    assert datetime_str != expecting.string.datetime.iso8601_hour()


@pytest.mark.parametrize(
    'datetime_str',
    (
        datetime.now().strftime('%Y-%m-%d'),
        datetime.utcnow().strftime('%Y-%m-%d'),
        datetime.utcnow().astimezone(timezone.max).strftime('%Y-%m-%d'),
        datetime.utcnow().astimezone(timezone.min).strftime('%Y-%m-%d'),
    )
)
def test_iso8601_day_matches(datetime_str: str):
    assert datetime_str == expecting.string.datetime.iso8601_day()


@pytest.mark.parametrize(
    'datetime_str',
    (
        '2023/10/11',
        '23-11-2023',
        '2023-11-31',
        '2023-15-15',
        datetime.now().strftime('%Y-%m-%dT%H'),
        datetime.now().strftime('%Y-%m-%dT%H:%M'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
        datetime.utcnow().astimezone(timezone.min).strftime('%Y-%m-%dT%H:%M:%S.%f%Z'),
        datetime.utcnow().astimezone(timezone.max).strftime('%Y-%m-%dT%H:%M:%S.%f%Z'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f+00000.0000'),
        'not even a date',
        None,
        2023,
        datetime.now(),
    )
)
def test_iso8601_day_does_not_match(datetime_str: str):
    assert datetime_str != expecting.string.datetime.iso8601_day()


@pytest.mark.parametrize(
    'datetime_str',
    (
        datetime.now().strftime('%Y-%m'),
        datetime.utcnow().strftime('%Y-%m'),
        datetime.utcnow().astimezone(timezone.max).strftime('%Y-%m'),
        datetime.utcnow().astimezone(timezone.min).strftime('%Y-%m'),
    )
)
def test_iso8601_month_matches(datetime_str: str):
    assert datetime_str == expecting.string.datetime.iso8601_month()


@pytest.mark.parametrize(
    'datetime_str',
    (
        '2023/10/11 13:01:10',
        '2023/10',
        '11-2023',
        '2023-15',
        datetime.now().strftime('%Y-%m-%d'),
        datetime.now().strftime('%Y-%m-%dT%H'),
        datetime.now().strftime('%Y-%m-%dT%H:%M'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
        datetime.utcnow().astimezone(timezone.min).strftime('%Y-%m-%dT%H:%M:%S.%f%Z'),
        datetime.utcnow().astimezone(timezone.max).strftime('%Y-%m-%dT%H:%M:%S.%f%Z'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f+00000.0000'),
        'not even a date',
        None,
        2023,
        datetime.now(),
    )
)
def test_iso8601_month_does_not_match(datetime_str: str):
    assert datetime_str != expecting.string.datetime.iso8601_month()


@pytest.mark.parametrize(
    'datetime_str',
    (
        datetime.now().strftime('%Y'),
        datetime.utcnow().strftime('%Y'),
        datetime.utcnow().astimezone(timezone.max).strftime('%Y'),
        datetime.utcnow().astimezone(timezone.min).strftime('%Y'),
    )
)
def test_iso8601_year_matches(datetime_str: str):
    assert datetime_str == expecting.string.datetime.iso8601_year()


@pytest.mark.parametrize(
    'datetime_str',
    (
        '2023/10/11 13:01:10',
        '0000',
        '-1',
        '23-11-2023T10:01:22',
        '2023-15-15T10:01:22',
        datetime.now().strftime('%Y-%m'),
        datetime.now().strftime('%Y-%m-%d'),
        datetime.now().strftime('%Y-%m-%dT%H'),
        datetime.now().strftime('%Y-%m-%dT%H:%M'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
        datetime.utcnow().astimezone(timezone.min).strftime('%Y-%m-%dT%H:%M:%S.%f%Z'),
        datetime.utcnow().astimezone(timezone.max).strftime('%Y-%m-%dT%H:%M:%S.%f%Z'),
        datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f+00000.0000'),
        'not even a date',
        None,
        2023,
        datetime.now(),
    )
)
def test_iso8601_year_does_not_match(datetime_str: str):
    assert datetime_str != expecting.string.datetime.iso8601_year()
