import requests

import config


def checkin():
    url = "https://123.zyzsphai.com/api/app/coop/connect"
    json ={}
    resp = config.GLOBAL_SESSION.post(url,json = json, proxies = config.PROXY)
    print(resp.json())