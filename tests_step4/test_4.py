import pytest


def test_test_me_twice(parametrized_fixture):
    assert False


@pytest.mark.parametrize(
    ("new_fixture_name",),
    [
        (10,),
        (20,)
    ]
)
def test_parametrize_the_test(new_fixture_name):
    assert new_fixture_name > 15


@pytest.mark.parametrize(
    ("plus_one", "expected"),
    [
        (1, 2),
        (44, 45),
    ],
    indirect=("plus_one",)  # what does True?
)
def test_indirect_parametrization(plus_one, expected):
    assert plus_one == expected


@pytest.mark.parametrize(
    ("parametrized_fixture", "expected"),
    [
        (1, 1),  # changed fixture parametrization
    ],
    indirect=("parametrized_fixture",)
)
def test_indirect_parametrization(parametrized_fixture, expected):
    assert parametrized_fixture == expected


@pytest.mark.usefixtures("parametrized_fixture")
def test_when_fixture_is_not_used_in_test():
    assert False


@pytest.mark.parametrize(
    ("expected",),
    [
        (42,),
        (45,),
    ]
)
def test_implement_your_fixture(your_fixture_comes_here, expected):
    assert your_fixture_comes_here == expected
