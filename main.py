#test分支
import requests

import config
from captcha import get_captcha
from checkin import checkin
from config import PROXY_API_URL
from helper_function import random_phone, random_true_name, generate_device_info, generate_fake_id
from identity import identity
from login import login
from proxy import get_usable_proxy
from register import register
import re
from paddleocr import PaddleOCR
if __name__ == "__main__":

    usable_proxy = get_usable_proxy(PROXY_API_URL)
    config.PROXY = usable_proxy
    phone = random_phone()
    name = "刘天明"
    idcard = "44022319871209031X"
    register(phone, name)
    login(phone)
    identity(name,idcard)
