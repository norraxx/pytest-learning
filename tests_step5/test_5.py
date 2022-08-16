import pytest

from some_evil_code import give_me_almighty_answer, give_me_answer


def test1():
    give_me_almighty_answer()


def test2():
    pass
    # give_me_answer()


def test3():
    with pytest.raises(Exception):
        raise Exception("What a Terrible Failure?!")


def test4():
    with pytest.raises(AssertionError):
        assert False

    with pytest.raises(Exception):
        assert True  # noqa pycharm has here a problem :-)


def test5():
    assert False


def test6():
    assert False


def test7():
    assert False


def test8():
    assert False


def test9():
    assert False


def test0():
    assert False
