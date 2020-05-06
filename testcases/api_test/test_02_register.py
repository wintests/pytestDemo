import pytest
import allure
from operation.user import register_user
from testcases.conftest import api_data
from common.logger import logger


@allure.step("步骤1 ==>> 注册用户")
def step_1(username, password, telephone, sex, address):
    logger.info("步骤1 ==>> 注册用户 ==>> {}, {}, {}, {}, {}".format(username, password, telephone, sex, address))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户注册模块")
class TestUserRegister():
    """用户注册"""

    @allure.story("用例--注册用户信息")
    @allure.description("该用例是针对获取用户注册接口的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title(
        "测试数据：【 {username}，{password}，{telephone}，{sex}，{address}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("username, password, telephone, sex, address, except_result, except_code, except_msg",
                             api_data["test_register_user"])
    @pytest.mark.usefixtures("delete_register_user")
    def test_register_user(self, username, password, telephone, sex, address, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = register_user(username, password, telephone, sex, address)
        step_1(username, password, telephone, sex, address)
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_02_register.py"])
