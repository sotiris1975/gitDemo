# Any pytest file should start with test_ or ends with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# method names should have sense
# -k stands for method names execution  -s logs in outputs  -v stands for more info metadata
# you can run specific file with py.test <filename>
# you can mark(tag) @pytest.mark.smoke and then run with -m
# you can skip test with @pytest.mark.skip
# pytest.mark.xfail
# fixtures are used as set up and tear down methods for test cases -
# conftest file generalize fixture and make it available to all test cases
# data driven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram(setup ):
    msg = "Hello"
    assert msg == "Hi", "test failed because string do not match"


def test_SecondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "addition do not match"


def test_fixtureDemo(setup):
    print("i will execute steps in fixtureDemo method")
    print("i will execute steps in fixtureDemo method1")
    print("i will execute steps in fixtureDemo method2")





