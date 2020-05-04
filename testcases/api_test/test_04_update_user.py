import pytest
from operation.user import update_user


@pytest.mark.usefixtures("update_user_telephone")
def test_update_user(login_fixture):
    user_info = login_fixture
    admin_user = user_info.get("login_info").get("username")
    token = user_info.get("login_info").get("token")
    result = update_user(4, admin_user, "123456", "13500010014", token=token, sex="1", address="深圳市坪山区")
    assert result.success is True, result.error

if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_04_update_user.py"])