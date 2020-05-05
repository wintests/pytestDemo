import pytest
import os
from api.user import user
from common.mysql_operate import db
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


base_data = get_data("base_data.yml")
api_data = get_data("api_test_data.yml")
scenario_data = get_data("scenario_test_data.yml")


@pytest.fixture(scope="session")
def login_fixture():
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "username": base_data["init_admin_user"]["username"],
        "password": base_data["init_admin_user"]["password"]
    }
    loginInfo = user.login(data=payload, headers=header)
    yield loginInfo.json()


@pytest.fixture(scope="function")
def insert_delete_user():
    """删除用户前，先在数据库插入一条用户数据"""
    # insert_sql = "INSERT INTO user(username, password, role, sex, telephone, address) " \
    #              "VALUES('test', '123456', '1', '1', '13488888888', '北京市海淀区')"
    insert_sql = base_data["init_sql"]["insert_delete_user"][0]
    db.execute_db(insert_sql)
    yield
    # 因为有些情况是不给删除管理员用户的，这种情况需要手动清理上面插入的数据
    del_sql = base_data["init_sql"]["insert_delete_user"][1]
    db.execute_db(del_sql)


@pytest.fixture(scope="function")
def delete_register_user():
    """注册用户前，先删除数据，用例执行之后，再次删除以清理数据"""
    print("前置清理操作--删除用户--准备注册新用户")
    del_sql = base_data["init_sql"]["delete_register_user"]
    db.execute_db(del_sql)
    yield
    print("后置清理操作--注册用户--删除注册的用户")
    db.execute_db(del_sql)


@pytest.fixture(scope="function")
def update_user_telephone():
    """修改用户前，因为手机号唯一，为了使用例重复执行，每次需要先修改手机号，再执行用例"""
    update_sql = base_data["init_sql"]["update_user_telephone"]
    db.execute_db(update_sql)
