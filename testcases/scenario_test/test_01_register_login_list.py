import pytest
from operation.user import register_user, login_user, get_one_user_info


@pytest.mark.usefixtures("delete_register_user")
def test_user_register_login_list(testcase_data):
    result = register_user(testcase_data["username"], testcase_data["password"], testcase_data["telephone"],
                           testcase_data["sex"], testcase_data["address"])
    assert result.success is True, result.error
    result = login_user(testcase_data["username"], testcase_data["password"])
    assert result.success is True, result.error
    result = get_one_user_info(testcase_data["username"])
    print("返回结果：{}".format(result.response.text))
    assert result.success == testcase_data["except_result"], result.error
    assert result.response.json().get("code") == testcase_data["except_code"]
    assert testcase_data["except_msg"] in result.msg


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_register_login_list.py"])
