import pytest
from requests import get


def test_non_ranged_success(server, data):
    api = '/sequence/'
    for seq in data:
        assert get(server + api + seq.sha512).text == seq.sequence


@pytest.mark.parametrize("query_input, output", [
    ("?stat=10&ed=67", 400),
    ("?ed=67", 400),
    ("?start=67", 400),
    ("?start=10&end=5", 501),
    ("?start=4", 400)

])
def test_ranged_errors(server, data, query_input, output):
    api = '/sequence/'
    for seq in data:
        assert get(server + api + seq.sha512 + "/" + query_input).status_code \
            == output


@pytest.mark.parametrize("header_input, output", [
    ({
        "Accept": "text/plain",
        "Range": "bytes=10-20"
    }, 206),
    ({"Accept": "text/vnd.ga4gh.seq.v1.0.0+plain"}, 200),
    ({}, 200),
])
def test_non_ranged_headers(server, data, header_input, output):
    api = '/sequence/'
    for seq in data:
        assert get(server + api + seq.sha512, headers=header_input).\
            status_code == output
