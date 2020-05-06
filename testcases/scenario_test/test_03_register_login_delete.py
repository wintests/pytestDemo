import pytest
import allure
from operation.user import register_user, login_user, delete_user
from common.logger import logger


@allure.step("步骤1 ==>> 注册用户")
def step_1(username, password, telephone, sex, address):
    logger.info("步骤1 ==>> 注册用户 ==>> {}, {}, {}, {}, {}".format(username, password, telephone, sex, address))


@allure.step("步骤2 ==>> 登录用户")
def step_2(username):
    logger.info("步骤2 ==>> 登录管理员用户：{}".format(username))


@allure.step("步骤3 ==>> 根据用户名来删除用户信息")
def step_3(username):
    logger.info("步骤3 ==>> 删除用户：{}".format(username))


@allure.severity(allure.severity_level.MINOR)
@allure.epic("针对业务场景的测试")
@allure.feature("场景：用户注册-用户登录-删除用户")
class TestRegLogDelete():

    @allure.story("用例--注册/登录/删除--预期成功")
    @allure.description("该用例是针对 注册-登录-删除 场景的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("用户注册登录删除-预期成功")
    @pytest.mark.multiple
    def test_user_register_login_delete_success(self, testcase_data):
        username = testcase_data["username"]
        password = testcase_data["password"]
        telephone = testcase_data["telephone"]
        sex = testcase_data["sex"]
        address = testcase_data["address"]
        admin_user = testcase_data["admin_user"]
        admin_pwd = testcase_data["admin_pwd"]
        except_result = testcase_data["except_result"]
        except_code = testcase_data["except_code"]
        except_msg = testcase_data["except_msg"]
        logger.info("*************** 开始执行用例 ***************")
        result = register_user(username, password, telephone, sex, address)
        step_1(username, password, telephone, sex, address)
        assert result.success is True, result.error
        result = login_user(admin_user, admin_pwd)
        step_2(username)
        assert result.success is True, result.error
        result = delete_user(username, admin_user, result.token)
        step_3(username)
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")


    """
    # 标记 strict=True 输出 allure 报告会报错，暂不处理
    # strict=True 可以让那些mark为xfail, 实际通显示XPASS的测试用例被置为失败
    """

    @allure.story("用例--注册/登录/删除--预期失败")
    @allure.description("该用例是针对 注册-登录-删除 场景的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("用户注册登录删除-预期失败")
    @pytest.mark.negative
    @pytest.mark.xfail(reason="xfail示例：预期失败的用例，如存在尚未解决的Bug等")
    @pytest.mark.usefixtures("delete_register_user")
    def test_user_register_login_delete_fail(self, testcase_data):
        username = testcase_data["username"]
        password = testcase_data["password"]
        telephone = testcase_data["telephone"]
        sex = testcase_data["sex"]
        address = testcase_data["address"]
        admin_user = testcase_data["admin_user"]
        admin_pwd = testcase_data["admin_pwd"]
        except_result = testcase_data["except_result"]
        except_code = testcase_data["except_code"]
        except_msg = testcase_data["except_msg"]
        logger.info("*************** 开始执行用例 ***************")
        result = register_user(username, password, telephone, sex, address)
        step_1(username, password, telephone, sex, address)
        assert result.success is True, result.error
        result = login_user(admin_user, admin_pwd)
        step_2(username)
        assert result.success is True, result.error
        result = delete_user(username, admin_user, result.token)
        step_3(username)
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_03_register_login_delete.py"])
