import pytest
from operation.user import register_user
from testcases.conftest import api_data
from common.logger import logger


@pytest.mark.single
@pytest.mark.parametrize("username, password, telephone, sex, address, except_result, except_code, except_msg",
                         api_data["test_register_user"])
@pytest.mark.usefixtures("delete_register_user")
def test_register_user(username, password, telephone, sex, address, except_result, except_code, except_msg):
    result = register_user(username, password, telephone, sex, address)
    logger.info("当前返回结果 ==>> {}".format(result.response.text))
    assert result.success == except_result, result.error
    assert result.response.status_code == 200
    assert result.success == except_result, result.error
    logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
    assert result.response.json().get("code") == except_code
    assert except_msg in result.msg

if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_02_register.py"])
