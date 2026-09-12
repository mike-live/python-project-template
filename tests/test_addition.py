from project.example_addition import addition


def test_addition():
    assert addition(2, 2) == 4
    assert addition(13, 27) == 40
    assert addition(-1, 1) == 0
