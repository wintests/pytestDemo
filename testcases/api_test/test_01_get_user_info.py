import pytest
from operation.user import get_all_user_info, get_one_user_info
from testcases.conftest import api_data
from common.logger import logger

@pytest.mark.single
@pytest.mark.parametrize("except_result, except_code, except_msg",
                         api_data["test_get_all_user_info"])
def test_get_all_user_info(except_result, except_code, except_msg):
    result = get_all_user_info()
    # print(result.__dict__)
    assert result.response.status_code == 200
    assert result.success == except_result, result.error
    logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code, result.response.json().get("code")))
    assert result.response.json().get("code") == except_code
    assert except_msg in result.msg


@pytest.mark.single
@pytest.mark.parametrize("username, except_result, except_code, except_msg",
                         api_data["test_get_get_one_user_info"])
def test_get_get_one_user_info(username, except_result, except_code, except_msg):
    result = get_one_user_info(username)
    # print(result.__dict__)
    assert result.response.status_code == 200
    assert result.success == except_result, result.error
    logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
    assert result.response.json().get("code") == except_code
    assert except_msg in result.msg


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_get_user_info.py"])
