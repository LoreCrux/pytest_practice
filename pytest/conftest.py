import pytest


@pytest.fixture(scope='class')
def setup():
    print('Running first, this is the setup fixture')
    yield


