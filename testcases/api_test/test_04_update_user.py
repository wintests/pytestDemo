import pytest
import allure
from operation.user import update_user
from testcases.conftest import api_data
from common.logger import logger


@allure.step("步骤1 ==>> 根据ID修改用户信息")
def step_1(id):
    logger.info("步骤1 ==>> 修改用户ID：{}".format(id))


@allure.step("前置登录步骤 ==>> 管理员登录")
def step_login(admin_user, token):
    logger.info("前置登录步骤 ==>> 管理员 {} 登录 ==>> 返回的 token 为：{}".format(admin_user, token))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户修改模块")
class TestUpdate():
    """修改用户"""

    @allure.story("用例--修改用户信息")
    @allure.description("该用例是针对获取用户修改接口的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title(
        "测试数据：【 {id}，{new_password}，{new_telephone}，{new_sex}，{new_address}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("id, new_password, new_telephone, new_sex, new_address, "
                             "except_result, except_code, except_msg",
                             api_data["test_update_user"])
    @pytest.mark.usefixtures("update_user_telephone")
    def test_update_user(self, login_fixture, id, new_password, new_telephone, new_sex, new_address,
                         except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        user_info = login_fixture
        admin_user = user_info.get("login_info").get("username")
        token = user_info.get("login_info").get("token")
        step_login(admin_user, token)
        result = update_user(id, admin_user, new_password, new_telephone, token, new_sex, new_address)
        step_1(id)
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_04_update_user.py"])
