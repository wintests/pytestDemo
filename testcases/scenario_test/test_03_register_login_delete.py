import pytest
from operation.user import register_user, login_user, delete_user


def test_user_register_login_delete_success(testcase_data):
    result = register_user(testcase_data["username"], testcase_data["password"], testcase_data["telephone"],
                           testcase_data["sex"], testcase_data["address"])
    assert result.success is True, result.error
    result = login_user(testcase_data["admin_user"], testcase_data["admin_pwd"])
    assert result.success is True, result.error
    result = delete_user(testcase_data["username"], testcase_data["admin_user"], result.token)
    print("返回结果：{}".format(result.response.text))
    assert result.success == testcase_data["except_result"], result.error
    assert result.response.json().get("code") == testcase_data["except_code"]
    assert testcase_data["except_msg"] in result.msg

@pytest.mark.skip(reason="xfail示例：预期失败的用例，如存在尚未解决的Bug等")
def test_user_register_login_delete_fail(testcase_data):
    result = register_user(testcase_data["username"], testcase_data["password"], testcase_data["telephone"],
                           testcase_data["sex"], testcase_data["address"])
    assert result.success is True, result.error
    result = login_user(testcase_data["admin_user"], testcase_data["admin_pwd"])
    assert result.success is True, result.error
    result = delete_user(testcase_data["username"], testcase_data["admin_user"], result.token)
    print("返回结果：{}".format(result.response.text))
    assert result.success == testcase_data["except_result"], result.error
    assert result.response.json().get("code") == testcase_data["except_code"]
    assert testcase_data["except_msg"] in result.msg


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_03_register_login_delete.py"])
