from core.result_base import ResultBase
from api.user import user
from common.logger import logger


def get_all_user_info():
    """
    获取全部用户信息
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    res = user.list_all_users()
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    return result


def get_one_user_info(username):
    """
    获取单个用户信息
    :param username:  用户名
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    res = user.list_one_user(username)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "查询用户 ==>> 接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("查看单个用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def register_user(username, password, telephone, sex="", address=""):
    """
    注册用户信息
    :param username: 用户名
    :param password: 密码
    :param telephone: 手机号
    :param sex: 性别
    :param address: 联系地址
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    json_data = {
        "username": username,
        "password": password,
        "sex": sex,
        "telephone": telephone,
        "address": address
    }
    header = {
        "Content-Type": "application/json"
    }
    res = user.register(json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("注册用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def login_user(username, password):
    """
    登录用户
    :param username: 用户名
    :param password: 密码
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    payload = {
        "username": username,
        "password": password
    }
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = user.login(data=payload, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
        result.token = res.json()["login_info"]["token"]
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def update_user(id, admin_user, new_password, new_telephone, token, new_sex="", new_address=""):
    """
    根据用户ID，修改用户信息
    :param id: 用户ID
    :param admin_user: 当前操作的管理员用户
    :param new_password: 新密码
    :param new_telephone: 新手机号
    :param token: 当前管理员用户的token
    :param new_sex: 新性别
    :param new_address: 新联系地址
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json"
    }
    json_data = {
        "admin_user": admin_user,
        "password": new_password,
        "token": token,
        "sex": new_sex,
        "telephone": new_telephone,
        "address": new_address
    }
    res = user.update(id, json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("修改用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def delete_user(username, admin_user, token):
    """
    根据用户名，删除用户信息
    :param username: 用户名
    :param admin_user: 当前操作的管理员用户
    :param token: 当前管理员用户的token
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    json_data = {
        "admin_user": admin_user,
        "token": token,
    }
    header = {
        "Content-Type": "application/json"
    }
    res = user.delete(username, json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("删除用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result
