import pytest
from operation.user import register_user


@pytest.mark.usefixtures("delete_register_user")
def test_user_register_login_list():
    result = register_user("测试test", "123456", "13599999999", sex="1", address="深圳市宝安区")
    assert result.success is True, result.error
    result = register_user("测试test", "123456", "13599999999", sex="1", address="深圳市宝安区")
    assert result.success is False, result.error
    assert "用户名已存在，注册失败" in result.response.json().get("msg")

if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_register_login_list.py"])
