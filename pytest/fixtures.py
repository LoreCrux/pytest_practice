import pytest


@pytest.mark.usefixtures("setup")
class TestFirstTests:

    def test_print(self):
        print('hello')

    def test_first_program(self):
        x = 5
        assert x > 10, 'FAILURE'

    def test_creditcard(self):
        print('I have a credit card')

    def test_creditcard_purchase(self):
        print('Looks at my credit card purchase')


def test_fixture_demo(setup):
    print('executing steps in fixture_demo method')
