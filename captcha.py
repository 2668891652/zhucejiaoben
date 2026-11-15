import requests

import config


def get_captcha():
    url1 = "https://6g1.gjjzzx.online/api/v1/auth/captcha"
    resp = config.GLOBAL_SESSION.get(url1,proxies = config.PROXY)
    return resp.json()["data"]["code"], resp.json()["data"]["id"]
