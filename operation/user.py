from core.result_base import ResultBase
from api.user import user


def get_all_user_info():
    result = ResultBase()
    res = user.list_all_users()
    result.success = False
    if res.json()["code"] == "0":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    return result


def get_one_user_info(username):
    result = ResultBase()
    res = user.list_one_user(username)
    result.success = False
    if res.json()["code"] == "0":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    return result


def register_user(username, password, telephone, sex="", address=""):
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
    return result


def login_user(username, password):
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
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    return result


def update_user(id, username, password, telephone, token, sex="", address=""):
    result = ResultBase()
    header = {
        "Content-Type": "application/json"
    }
    json_data = {
        "username": username,
        "password": password,
        "token": token,
        "sex": sex,
        "telephone": telephone,
        "address": address
    }
    res = user.update(id, json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    return result


def delete_user(id, username, token):
    result = ResultBase()
    json_data = {
        "username": username,
        "token": token,
    }
    header = {
        "Content-Type": "application/json"
    }
    res = user.delete(id, json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    return result
