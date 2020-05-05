import pytest
from operation.user import register_user, login_user, delete_user
from common.logger import logger


@pytest.mark.multiple
def test_user_register_login_delete_success(testcase_data):
    result = register_user(testcase_data["username"], testcase_data["password"], testcase_data["telephone"],
                           testcase_data["sex"], testcase_data["address"])
    logger.info("注册用户 ==>> 当前返回结果 ==>> {}".format(result.response.text))
    assert result.success is True, result.error
    result = login_user(testcase_data["admin_user"], testcase_data["admin_pwd"])
    logger.info("登录管理员用户 ==>> 当前返回结果 ==>> {}".format(result.response.text))
    assert result.success is True, result.error
    result = delete_user(testcase_data["username"], testcase_data["admin_user"], result.token)
    logger.info("删除新用户 ==>> 当前返回结果 ==>> {}".format(result.response.text))
    assert result.success == testcase_data["except_result"], result.error
    logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(testcase_data["except_code"], result.response.json().get("code")))
    assert result.response.json().get("code") == testcase_data["except_code"]
    assert testcase_data["except_msg"] in result.msg


# strict=True 可以让那些mark为xfail, 实际通显示XPASS的测试用例被置为失败
@pytest.mark.negative
@pytest.mark.xfail(reason="xfail示例：预期失败的用例，如存在尚未解决的Bug等")
@pytest.mark.usefixtures("delete_register_user")
def test_user_register_login_delete_fail(testcase_data):
    result = register_user(testcase_data["username"], testcase_data["password"], testcase_data["telephone"],
                           testcase_data["sex"], testcase_data["address"])
    logger.info("注册用户 ==>> 当前返回结果 ==>> {}".format(result.response.text))
    assert result.success is True, result.error
    result = login_user(testcase_data["admin_user"], testcase_data["admin_pwd"])
    logger.info("登录管理员用户 ==>> 当前返回结果 ==>> {}".format(result.response.text))
    assert result.success is True, result.error
    result = delete_user(testcase_data["username"], testcase_data["admin_user"], result.token)
    logger.info("删除新用户 ==>> 当前返回结果 ==>> {}".format(result.response.text))
    assert result.success == testcase_data["except_result"], result.error
    logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(testcase_data["except_code"], result.response.json().get("code")))
    assert result.response.json().get("code") == testcase_data["except_code"]
    assert testcase_data["except_msg"] in result.msg


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_03_register_login_delete.py"])
