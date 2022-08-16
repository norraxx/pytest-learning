from some_evil_code import give_me_almighty_answer


def test_some_holy_function():
    """
    It is good practice to write at the beginning of the test, what do you test, and why.
    """
    assert give_me_almighty_answer() == 42, "Almighty Answer is not 42?"
