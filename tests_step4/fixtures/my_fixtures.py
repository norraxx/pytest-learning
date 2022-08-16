from pytest import fixture

__all__ = ('parametrized_fixture', 'plus_one')


@fixture(params=["a", "b"])
def parametrized_fixture(request):
    return request.param


@fixture
def plus_one(request):
    return request.param + 1

