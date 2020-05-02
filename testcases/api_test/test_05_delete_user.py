import pytest
from operation.user import delete_user


def test_delete_user(login_fixture, insert_delete_user):
    username = login_fixture.get("login_info").get("username")
    token = login_fixture.get("login_info").get("token")
    result = delete_user(7, username, token)
    assert result.success is True, result.error

if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_04_update_user.py"])