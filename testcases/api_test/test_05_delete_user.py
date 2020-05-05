import pytest
from operation.user import delete_user
from testcases.conftest import api_data


@pytest.mark.parametrize("username, except_result, except_code, except_msg",
                         api_data["test_delete_user"])
@pytest.mark.usefixtures("insert_delete_user")
def test_delete_user(login_fixture, username, except_result, except_code, except_msg):
    user_info = login_fixture
    admin_user = user_info.get("login_info").get("username")
    token = user_info.get("login_info").get("token")
    result = delete_user(username, admin_user, token)
    print("返回结果：{}".format(result.response.text))
    assert result.success == except_result, result.error
    assert result.response.status_code == 200
    assert result.success == except_result, result.error
    assert result.response.json().get("code") == except_code
    assert except_msg in result.msg


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_05_delete_user.py"])