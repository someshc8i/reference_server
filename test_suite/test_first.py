from utils import get
import pytest


@pytest.mark.non_circular
@pytest.mark.parametrize("query_imput, output", [
    ("?stat=10&ed=67", 400),
    ("?ed=67", 400),
    ("?start=67", 400),
    ("?start=10&end=5", 501),
    ("?start=4", 400)

])
def test_errors_start_end_queries_NC(server, data, query_imput, output):
    api = "/sequence/" + data["NC"]["trunc512"] + "/" + query_imput
    assert get(server, api).status_code == output


@pytest.mark.non_circular
@pytest.mark.parametrize("query_imput, expected_status_code", [
    ("?stat=10&ed=67", 400),
    ("?ed=67", 400),
    ("?start=67", 400),
    ("?start=10&end=5", 501),
    ("?start", 400)
])
def test_errors_start_end_queries_VI(
        server, data, query_imput, expected_status_code):
    api = "/sequence/" + data["VI"]["trunc512"] + "/" + query_imput
    assert get(server, api).status_code == expected_status_code
