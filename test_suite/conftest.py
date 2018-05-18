import pytest
from utils import get_chr_obj


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
    return request.config.getoption("--server")
