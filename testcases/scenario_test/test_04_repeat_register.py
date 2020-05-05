import pytest
from operation.user import register_user
from common.logger import logger


@pytest.mark.single
@pytest.mark.usefixtures("delete_register_user")
def test_user_repeat_register(testcase_data):
    result = register_user(testcase_data["username"], testcase_data["password"], testcase_data["telephone"],
                           testcase_data["sex"], testcase_data["address"])
    logger.info("注册用户 ==>> 当前返回结果 ==>> {}".format(result.response.text))
    assert result.success is True, result.error
    result = register_user(testcase_data["username"], testcase_data["password"], testcase_data["telephone"],
                           testcase_data["sex"], testcase_data["address"])
    logger.info("再次注册用户 ==>> 当前返回结果 ==>> {}".format(result.response.text))
    assert result.success == testcase_data["except_result"], result.error
    logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(testcase_data["except_code"], result.response.json().get("code")))
    assert result.response.json().get("code") == testcase_data["except_code"]
    assert testcase_data["except_msg"] in result.msg

if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_04_repeat_register.py"])
