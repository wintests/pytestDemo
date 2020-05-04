import pytest
from operation.user import register_user, login_user, delete_user


def test_user_register_login_delete_success():
    result = register_user("测试test", "123456", "13599999999", sex="1", address="深圳市宝安区")
    assert result.success is True, result.error
    result = login_user("wintest", "123456")
    assert result.success is True, result.error
    result = delete_user("测试test", "wintest", result.token)
    assert result.success is True, result.error
    assert "删除用户信息成功" in result.response.json().get("msg")

def test_user_register_login_delete_fail_1(delete_register_user):
    result = register_user("测试test", "123456", "13599999999", sex="1", address="深圳市宝安区")
    assert result.success is True, result.error
    result = login_user("wintest", "123456")
    assert result.success is True, result.error
    result = delete_user("test", "wintest", result.token)
    assert result.success is False, result.error
    assert "用户名不存在" in result.response.json().get("msg")

def test_user_register_login_delete_fail_2(delete_register_user):
    result = register_user("测试test", "123456", "13599999999", sex="1", address="深圳市宝安区")
    assert result.success is True, result.error
    result = login_user("测试test", "123456")
    assert result.success is True, result.error
    result = delete_user("test", "测试test", result.token)
    assert result.success is False, result.error
    assert "当前用户不是管理员用户" in result.response.json().get("msg")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_03_register_login_delete.py"])
