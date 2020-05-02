import pytest
from config.settings import username, password
from api.user import user

@pytest.fixture(scope="session")
def login_fixture():
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "username": username,
        "password": password
    }
    loginInfo = user.login(data=payload, headers=header)
    yield loginInfo.json()

@pytest.fixture(scope="session")
def unlogin_fixture():
    pass