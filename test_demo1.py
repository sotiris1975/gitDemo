# Any pytest file should start with test_ or ends with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# @pytest.mark.xfail
import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])