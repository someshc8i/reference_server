import pytest
from utils import get_seq_obj


@pytest.fixture(scope='session')
def data():
    data = []
    data.append(get_seq_obj("I"))
    data.append(get_seq_obj("VI"))
    data.append(get_seq_obj("NC"))
    return data


def pytest_addoption(parser):
    parser.addoption("--server", type="string")


@pytest.fixture(scope='session')
def server(request):
    return 'http://' + request.config.getoption("--server")
