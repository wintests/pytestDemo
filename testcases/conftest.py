import pytest
from api.user import user
from common.mysql_operate import db


@pytest.fixture(scope="session")
def login_fixture():
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "username": "wintest",
        "password": "123456"
    }
    loginInfo = user.login(data=payload, headers=header)
    yield loginInfo.json()

@pytest.fixture(scope="function")
def insert_delete_user():
    """删除用户前，先在数据库插入一条用户数据"""
    insert_sql = "INSERT INTO user(username, password, role, sex, telephone, address) " \
                 "VALUES('test', '123456', '1', '1', '13488888888', '北京市海淀区')"
    db.execute_db(insert_sql)

@pytest.fixture(scope="function")
def delete_register_user():
    """注册用户前，先删除数据，用例执行之后，再次删除以清理数据"""
    print("前置清理操作")
    del_sql = "DELETE FROM user WHERE username = '测试test'"
    db.execute_db(del_sql)
    yield
    print("后置清理操作")
    db.execute_db(del_sql)

@pytest.fixture(scope="function")
def update_user_telephone():
    """修改用户前，因为手机号唯一，为了使用例重复执行，每次需要先修改手机号，再执行用例"""
    update_sql = "UPDATE user SET telephone = '13500010004' WHERE username = 'wintest4'"
    db.execute_db(update_sql)