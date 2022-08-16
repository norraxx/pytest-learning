import pytest


def test_numbers():
    assert give_me_one == 1
    assert give_me_five == 5
    assert give_me_six == 6


def test_yield_numbers(yield_me_five):
    assert yield_me_five == 5
    assert False


@pytest.mark.usefixtures("class_living_fixture")
class TestClass1:
    def test_case1(self, class_living_fixture):
        print(class_living_fixture)
        assert class_living_fixture
        assert False

    def test_case2(self, class_living_fixture):
        print(class_living_fixture)
        assert class_living_fixture
        assert False


class TestClass2:
    @pytest.mark.usefixtures("class_living_fixture")
    def test_case3(self, class_living_fixture):
        print(class_living_fixture)
        assert class_living_fixture
        assert False

    @pytest.mark.usefixtures("class_living_fixture")
    def test_case4(self, class_living_fixture):
        print(class_living_fixture)
        assert class_living_fixture
        assert False
