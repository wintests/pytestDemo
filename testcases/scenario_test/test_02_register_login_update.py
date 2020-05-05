import pytest
from operation.user import register_user, login_user, get_one_user_info, update_user


@pytest.mark.usefixtures("delete_register_user")
def test_user_register_login_update_success(testcase_data):
    result = register_user(testcase_data["register"]["username"], testcase_data["register"]["password"],
                           testcase_data["register"]["telephone"], testcase_data["register"]["sex"],
                           testcase_data["register"]["address"])
    assert result.success is True, result.error
    result = login_user(testcase_data["login"]["admin_user"], testcase_data["login"]["admin_pwd"])
    assert result.success is True, result.error
    admin_token = result.token
    result = get_one_user_info(testcase_data["register"]["username"])
    id = result.response.json().get("data")[0].get("id")
    assert result.success is True, result.error
    result = update_user(id, testcase_data["login"]["admin_user"], testcase_data["update"]["new_password"],
                         testcase_data["update"]["new_telephone"], admin_token, testcase_data["update"]["new_sex"],
                         testcase_data["update"]["new_address"])
    print("返回结果：{}".format(result.response.text))
    assert result.success == testcase_data["except_result"], result.error
    assert result.response.json().get("code") == testcase_data["except_code"]
    assert testcase_data["except_msg"] in result.msg


@pytest.mark.usefixtures("delete_register_user")
def test_user_register_login_update_fail(testcase_data):
    result = register_user(testcase_data["register"]["username"], testcase_data["register"]["password"],
                           testcase_data["register"]["telephone"], testcase_data["register"]["sex"],
                           testcase_data["register"]["address"])
    assert result.success is True, result.error
    result = login_user(testcase_data["login"]["admin_user"], testcase_data["login"]["admin_pwd"])
    assert result.success is True, result.error
    admin_token = result.token
    result = get_one_user_info(testcase_data["register"]["username"])
    id = result.response.json().get("data")[0].get("id")
    assert result.success is True, result.error
    result = update_user(id + 1, testcase_data["login"]["admin_user"], testcase_data["update"]["new_password"],
                         testcase_data["update"]["new_telephone"], admin_token, testcase_data["update"]["new_sex"],
                         testcase_data["update"]["new_address"])
    print("返回结果：{}".format(result.response.text))
    assert result.success == testcase_data["except_result"], result.error
    assert result.response.json().get("code") == testcase_data["except_code"]
    assert testcase_data["except_msg"] in result.msg


@pytest.mark.skip(reason="skip跳过示例：暂时无法运行该用例")
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
    print("返回结果：{}".format(result.response.text))
    assert result.success is False, result.error
    assert "手机号已被注册" in result.response.json().get("msg")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_02_register_login_update.py"])
