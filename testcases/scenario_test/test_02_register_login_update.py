import pytest
from operation.user import register_user, login_user, get_one_user_info, update_user


def test_user_register_login_update_success(delete_register_user):
    result = register_user("测试test", "123456", "13599999999", sex="1", address="深圳市宝安区")
    assert result.success is True, result.error
    result = login_user("wintest", "123456")
    assert result.success is True, result.error
    token = result.token
    result = get_one_user_info("测试test")
    print(result.response.json())
    id = result.response.json().get("data")[0].get("id")
    assert result.success is True, result.error
    result = update_user(id, "wintest", "123456", "13599999998", token=token, sex="1", address="深圳市坪山区")
    assert result.success is True, result.error
    assert "修改用户信息成功" in result.response.json().get("msg")

def test_user_register_login_update_fail_1(delete_register_user):
    result = register_user("测试test", "123456", "13599999999", sex="1", address="深圳市宝安区")
    assert result.success is True, result.error
    result = login_user("wintest", "123456")
    assert result.success is True, result.error
    token = result.token
    result = get_one_user_info("测试test")
    assert result.success is True, result.error
    id = result.response.json().get("data")[0].get("id")
    result = update_user(int(id) + 1, "wintest", "123456", "13599999998", token=token, sex="1", address="深圳市坪山区")
    assert result.success is False, result.error
    assert "用户ID不存在" in result.response.json().get("msg")

def test_user_register_login_update_fail_2(delete_register_user):
    result = register_user("测试test", "123456", "13599999999", sex="1", address="深圳市宝安区")
    assert result.success is True, result.error
    result = login_user("wintest", "123456")
    assert result.success is True, result.error
    token = result.token
    result = get_one_user_info("测试test")
    id = result.response.json().get("data")[0].get("id")
    assert result.success is True, result.error
    result = get_one_user_info("wintest")
    telephone = result.response.json().get("data")[0].get("telephone")
    result = update_user(id, "wintest", "123456", telephone, token=token, sex="1", address="深圳市坪山区")
    assert result.success is False, result.error
    assert "手机号已被注册" in result.response.json().get("msg")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_02_register_login_update.py"])
