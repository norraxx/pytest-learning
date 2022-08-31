import pytest

from some_evil_code import foo, Foo
from mock import patch, Mock
import time


def test_mock_object(fake_target_bar, mocker):
    with fake_target_bar(foo):
        assert foo.bar() == 20
    assert foo.bar() == 10

    with patch.object(foo, "bar", return_value=20):
        assert foo.bar() == 20

    assert foo.bar() == 10

    with mocker.patch.object(foo, "bar", return_value=20):
        assert foo.bar() == 20

    assert foo.bar() == 20  # ]:->

    assert False


def test_mock_class_method(mocker):
    with patch.object(Foo, "bar", return_value=20) as mock:
        assert Foo().bar() == 20
    mock.assert_called()

    assert Foo().bar() == 10

    with mocker.patch.object(Foo, "bar", return_value=20):
        assert Foo().bar() == 20

    assert Foo().bar() == 20

    assert False


def test_mock_function(monkeypatch):
    monkeypatch.setattr(time, "time", lambda: 0)
    assert time.time() == 0

    with patch.object(Foo, "bar", return_value=20) as mock:
        assert Foo().bar() == 20
    mock.assert_called()

    assert False


def test_mock_as_exception():
    with pytest.raises(Exception):
        mock = Mock(side_effect=Exception("Python rocks!"))
        mock()
    mock.assert_called()

    assert False
