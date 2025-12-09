import pytest

import expecting


@pytest.mark.parametrize(
    'url, expected_scheme',
    (
        ('http://example.com', 'http'),
        ('https://example.com', 'https'),
        ('file:///usr/data/test', 'file'),
        ('mongo+srv://mymongo.example', 'mongo+srv'),
    )
)
def test_url_with_scheme_matches(url: str, expected_scheme: str) -> None:
    assert url == expecting.string.url.with_scheme(expected_scheme)


@pytest.mark.parametrize(
    'url, expected_scheme',
    (
        (None, 'http'),
        ('', 'https'),
        ('file+links:///usr/data/test', 'file'),
    )
)
def test_url_with_scheme_does_not_match(url: str, expected_scheme: str) -> None:
    assert url != expecting.string.url.with_scheme(expected_scheme)


@pytest.mark.parametrize(
    'url, expected_netloc',
    (
        ('http://example.com', 'example.com'),
        ('https://user:pass@example.com:8080', 'user:pass@example.com:8080'),
        ('ftp://ftp.example.org', 'ftp.example.org'),
        ('http://192.168.1.1', '192.168.1.1'),
    )
)
def test_url_with_netloc_matches(url: str, expected_netloc: str) -> None:
    assert url == expecting.string.url.with_netloc(expected_netloc)


@pytest.mark.parametrize(
    'url, expected_netloc',
    (
        (None, 'example.com'),
        ('', 'example.com'),
        ('http://wrong.com', 'example.com'),
        ('not a url', 'example.com'),
    )
)
def test_url_with_netloc_does_not_match(url: str, expected_netloc: str) -> None:
    assert url != expecting.string.url.with_netloc(expected_netloc)


@pytest.mark.parametrize(
    'url, expected_path',
    (
        ('http://example.com/path/to/resource', '/path/to/resource'),
        ('https://example.com/', '/'),
        ('https://example.com', ''),
        ('file:///usr/local/bin', '/usr/local/bin'),
        ('http://example.com/path', '/path'),
    )
)
def test_url_with_path_matches(url: str, expected_path: str) -> None:
    assert url == expecting.string.url.with_path(expected_path)


@pytest.mark.parametrize(
    'url, expected_path',
    (
        (None, '/path'),
        ('', '/path'),
        ('http://example.com/wrong', '/path'),
        ('not a url', '/path'),
    )
)
def test_url_with_path_does_not_match(url: str, expected_path: str) -> None:
    assert url != expecting.string.url.with_path(expected_path)


@pytest.mark.parametrize(
    'url, expected_query',
    (
        ('http://example.com?key=value', 'key=value'),
        ('https://example.com?foo=bar&baz=qux', 'foo=bar&baz=qux'),
        ('http://example.com/path?search=test', 'search=test'),
        ('http://example.com?', ''),
    )
)
def test_url_with_query_matches(url: str, expected_query: str) -> None:
    assert url == expecting.string.url.with_query(expected_query)


@pytest.mark.parametrize(
    'url, expected_query',
    (
        (None, 'key=value'),
        ('', 'key=value'),
        ('http://example.com?wrong=value', 'key=value'),
        ('not a url', 'key=value'),
    )
)
def test_url_with_query_does_not_match(url: str, expected_query: str) -> None:
    assert url != expecting.string.url.with_query(expected_query)


@pytest.mark.parametrize(
    'url, expected_fragment',
    (
        ('http://example.com#section', 'section'),
        ('https://example.com/path#anchor', 'anchor'),
        ('http://example.com#', ''),
        ('ftp://example.com/file#fragment', 'fragment'),
    )
)
def test_url_with_fragment_matches(url: str, expected_fragment: str) -> None:
    assert url == expecting.string.url.with_fragment(expected_fragment)


@pytest.mark.parametrize(
    'url, expected_fragment',
    (
        (None, 'section'),
        ('', 'section'),
        ('http://example.com#wrong', 'section'),
        ('not a url', 'section'),
    )
)
def test_url_with_fragment_does_not_match(url: str, expected_fragment: str) -> None:
    assert url != expecting.string.url.with_fragment(expected_fragment)


@pytest.mark.parametrize(
    'url',
    (
        'http://example.com',
        'https://example.com:8080/path?query=value#fragment',
        'ftp://ftp.example.org/file',
        'file:///usr/local/bin',
        'ws://websocket.example.com',
    )
)
def test_url_any_matches(url: str) -> None:
    assert url == expecting.string.url.any()


@pytest.mark.parametrize(
    'url',
    (
        None,
        '',
        'not a url',
        'example.com',
        123,
        True,
        False,
    )
)
def test_url_any_does_not_match(url) -> None:
    assert url != expecting.string.url.any()
