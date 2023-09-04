import pytest



@pytest.fixture(scope="class")
def setup():
    print("i will be executing first")
    yield
    print("i will execute last ")

@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Sotiris", "Balatzis", "sotirisbalatzis@gmail.com"]

@pytest.fixture(params=[("chrome", "Sotiris", "Balatzis"), ("firefox", "Balatzis"), ("IE", "DD")])
def crossBrowser(request):
    return request.param

