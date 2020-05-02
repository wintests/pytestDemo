import pytest
from operation.user import update_user


def test_update_user(login_fixture, update_user_telephone):
    username = login_fixture.get("login_info").get("username")
    token = login_fixture.get("login_info").get("token")
    result = update_user(4, username, "123456", "13500010004", token=token, sex="0", address="")
    assert result.success is True, result.error

if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_04_update_user.py"])