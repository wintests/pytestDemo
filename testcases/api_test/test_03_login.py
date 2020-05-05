import pytest
from operation.user import login_user
from testcases.conftest import api_data
from common.logger import logger


@pytest.mark.single
@pytest.mark.parametrize("username, password, except_result, except_code, except_msg",
                         api_data["test_login_user"])
def test_login_user(username, password, except_result, except_code, except_msg):
    result = login_user(username, password)
    logger.info("当前返回结果 ==>> {}".format(result.response.text))
    assert result.success == except_result, result.error
    assert result.response.status_code == 200
    assert result.success == except_result, result.error
    logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
    assert result.response.json().get("code") == except_code
    assert except_msg in result.msg


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_03_login.py"])
