import pytest
import tempfile
import os
import itertools

import retrieval


@pytest.fixture
def test_urls():
    return [
            "https://github.githubassets.com/favicons/favicon.png",
            "https://about.gitlab.com/ico/favicon.ico",
            "https://www.chess.com/bundles/web/favicons/favicon-32x32.c2a8280d.png",
            ]

def test_local_path(test_urls):
    dir_path = "fake"
    received = retrieval._local_path(test_urls[0], dir_path)
    expected = os.path.join(dir_path, "favicon.png")
    assert received == expected


def test_time_parse():
    import time
    time.strptime("Sat, 05 Dec 2020 10:18:06 GMT", "%a, %d %b %Y %H:%M:%S %Z")

@pytest.mark.web_test
def test_get_mod_time(test_urls):
    times = [ retrieval.get_mod_time(url) for url in test_urls]
    times.append(retrieval.get_mod_time(retrieval.ROOT_URL))
    for ts in times:
        print(ts)
    for comb in itertools.combinations(times, 2):
        assert comb[0] != comb[1]

@pytest.mark.web_test
def test_build_local_cache(test_urls):
    with tempfile.TemporaryDirectory() as tempdir:
        #print(tempdir)
        #print(dir(tempdir))
        retrieval.build_local_cache(test_urls, tempdir)

