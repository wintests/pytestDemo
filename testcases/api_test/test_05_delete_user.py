import pytest
from operation.user import delete_user


@pytest.mark.usefixtures("insert_delete_user")
def test_delete_user(login_fixture):
    user_info = login_fixture
    admin_user = user_info.get("login_info").get("username")
    token = user_info.get("login_info").get("token")
    result = delete_user("test", admin_user, token)
    assert result.success is True, result.error

if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_05_delete_user.py"])