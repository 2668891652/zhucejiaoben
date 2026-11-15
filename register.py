import config
from helper_function import generate_device_info


def register(phone,name):
    url = "https://www.ceic.cam/mobile/login/register/sign/9658267.shtm"
    payload = {
        "username": name,
        "mobile": phone,
        "password": "wcnm1234",
        "relpy": "wcnm1234",
        "invita_code": "9658267"
    }
    resp = config.GLOBAL_SESSION.post(url, data=payload, proxies=config.PROXY)
    print(resp.json())
