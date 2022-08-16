from random import randint

from pytest import fixture, yield_fixture


@fixture
def give_me_one():
    return 1


@fixture
def give_me_five(give_me_one):
    return give_me_one * 5


@fixture
def give_me_six(give_me_five):
    return give_me_five + 1


@yield_fixture
def yield_me_five(give_me_five):
    """
    Yield fixture is deprecated, don't use it.
    """
    print('this is the magic before in preparation phase')
    yield give_me_five
    print('this is the magic after test execution phase')


@fixture
def yield_me_six(give_me_six):
    """
    This fixture is allowed
    """
    print('this is the magic before in preparation phase')
    yield give_me_six
    print('this is the magic after test execution phase')


@fixture(autouse=True)
def long_living_fixture():
    print("May the Force be with you")


@fixture(scope="class")
def class_living_fixture():
    return randint(0, 100)
