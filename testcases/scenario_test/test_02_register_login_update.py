import pytest
import allure
from operation.user import register_user, login_user, get_one_user_info, update_user
from common.logger import logger


@allure.step("步骤1 ==>> 注册用户")
def step_1(username, password, telephone, sex, address):
    logger.info("步骤1 ==>> 注册用户 ==>> {}, {}, {}, {}, {}".format(username, password, telephone, sex, address))


@allure.step("步骤2 ==>> 登录用户")
def step_2(username):
    logger.info("步骤2 ==>> 登录管理员用户：{}".format(username))


@allure.step("步骤3 ==>> 查看新注册用户ID")
def step_3(id):
    logger.info("步骤3 ==>> 查看新注册用户ID：{}".format(id))


@allure.step("步骤4 ==>> 根据ID修改用户信息")
def step_4(id):
    logger.info("步骤4 ==>> 修改用户ID：{}".format(id))


@allure.severity(allure.severity_level.BLOCKER)
@allure.epic("针对业务场景的测试")
@allure.feature("场景：用户注册-用户登录-修改用户")
class TestRegLogUpdate():

    @allure.story("用例--注册/登录/修改--预期成功")
    @allure.description("该用例是针对 注册-登录-修改 场景的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("用户注册登录修改--预期成功")
    @pytest.mark.multiple
    @pytest.mark.usefixtures("delete_register_user")
    def test_user_register_login_update_success(self, testcase_data):
        username = testcase_data["register"]["username"]
        password = testcase_data["register"]["password"]
        telephone = testcase_data["register"]["telephone"]
        sex = testcase_data["register"]["sex"]
        address = testcase_data["register"]["address"]
        admin_user = testcase_data["login"]["admin_user"]
        admin_pwd = testcase_data["login"]["admin_pwd"]
        new_password = testcase_data["update"]["new_password"]
        new_telephone = testcase_data["update"]["new_telephone"]
        new_sex = testcase_data["update"]["new_sex"]
        new_address = testcase_data["update"]["new_address"]
        except_result = testcase_data["except_result"]
        except_code = testcase_data["except_code"]
        except_msg = testcase_data["except_msg"]
        logger.info("*************** 开始执行用例 ***************")
        result = register_user(username, password, telephone, sex, address)
        step_1(username, password, telephone, sex, address)
        assert result.success is True, result.error
        result = login_user(admin_user, admin_pwd)
        step_2(admin_user)
        assert result.success is True, result.error
        admin_token = result.token
        result = get_one_user_info(username)
        id = result.response.json().get("data")[0].get("id")
        step_3(id)
        assert result.success is True, result.error
        result = update_user(id, admin_user, new_password, new_telephone, admin_token, new_sex, new_address)
        step_4(id)
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--注册/登录/修改--预期失败")
    @allure.description("该用例是针对 注册-登录-修改 场景的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("用户注册登录修改--预期失败")
    @pytest.mark.multiple
    @pytest.mark.usefixtures("delete_register_user")
    def test_user_register_login_update_fail(self, testcase_data):
        username = testcase_data["register"]["username"]
        password = testcase_data["register"]["password"]
        telephone = testcase_data["register"]["telephone"]
        sex = testcase_data["register"]["sex"]
        address = testcase_data["register"]["address"]
        admin_user = testcase_data["login"]["admin_user"]
        admin_pwd = testcase_data["login"]["admin_pwd"]
        new_password = testcase_data["update"]["new_password"]
        new_telephone = testcase_data["update"]["new_telephone"]
        new_sex = testcase_data["update"]["new_sex"]
        new_address = testcase_data["update"]["new_address"]
        except_result = testcase_data["except_result"]
        except_code = testcase_data["except_code"]
        except_msg = testcase_data["except_msg"]
        logger.info("*************** 开始执行用例 ***************")
        result = register_user(username, password, telephone, sex, address)
        step_1(username, password, telephone, sex, address)
        assert result.success is True, result.error
        result = login_user(admin_user, admin_pwd)
        step_2(admin_user)
        assert result.success is True, result.error
        admin_token = result.token
        result = get_one_user_info(username)
        id = result.response.json().get("data")[0].get("id")
        step_3(id)
        assert result.success is True, result.error
        result = update_user(id + 1, admin_user, new_password, new_telephone, admin_token, new_sex, new_address)
        step_4(id)
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")

    @pytest.mark.negative
    @pytest.mark.skip(reason="skip跳过示例：暂时无法运行该用例")
    def test_user_register_login_update_fail_2(self):
        pass


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_02_register_login_update.py"])
