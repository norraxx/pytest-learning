def our_magic_function():
    return 42


def test_asert_true():
    """
    We're testing, that pytest passes the tests, that have some truthy assertions.
    """
    assert True
    assert 1
    assert {"a": 1}
    assert [1, 2, 3]
    assert False  # You'll never be 100% sure, if test was called, unless you'll make it explicitly fail.


def test_asert_false():
    """
    Testing the reaction on false and falsy objects
    """
    assert False, "assert raises AssertionError, and this is his message"


def test_asert_false2():
    """
    Testing the reaction on falsy objects
    """
    res = our_magic_function()
    assert res == 24, "Expecting the 24, but got {}".format(res)
