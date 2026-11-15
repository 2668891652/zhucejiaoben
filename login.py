import config


def login(phone):
    url = "https://www.ceic.cam/login/login.shtml"
    data = {
        "username":phone,
        "password":"wcnm1234"
    }
    resp = config.GLOBAL_SESSION.post(url,json=data,proxies=config.PROXY)
    print(resp.text)
    # if resp.json()["message"] == "登录成功":
