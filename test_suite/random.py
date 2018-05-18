import pytest
from utils import get_chr_obj

DATA = {
    "I": None,
    "VI": None,
    "NC": None
}


@pytest.fixture(scope='session')
def data():
    data = {
        "I": get_chr_obj("I"),
        "VI": get_chr_obj("VI"),
        "NC": get_chr_obj("NC")
    }
    return data


def pytest_addoption(parser):
    parser.addoption("--server", type="string")


@pytest.fixture(scope='session')
def server(request):
    DATA["I"] = get_chr_obj("I")
    DATA["VI"] = get_chr_obj("VI")
    DATA["NC"] = get_chr_obj("NC")
    return request.config.getoption("--server")
