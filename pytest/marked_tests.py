import pytest


@pytest.mark.smoke
def test_marker_one():
    marking = 'mark'
    name = 'mark'
    assert marking == name, "This name is incorrect"


@pytest.mark.skip
def test_marker_two():
    marking = 'mark'
    name = 'mark'
    assert marking == name, "This name is incorrect"


@pytest.mark.xfail
def test_marker_three():
    marking = 'mark'
    name = 'mark'
    assert marking == name, "This name is incorrect"
