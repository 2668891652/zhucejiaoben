import requests

import config


def get_one_proxy(api_url: str):
    """
    调用代理API获取1个ip，对应你截图提取数量=1，返回 {"ip":"xxx","port":"xxx"} 或者None
    :param api_url: 你的订单生成的API链接
    :return: dict/None
    """
    try:
        resp = requests.get(api_url, timeout=10)
        data = resp.json()
        if data.get("code") == "0" and len(data.get("obj", [])) > 0:
            proxy_info = data["obj"][0]
            return proxy_info
        return None
    except Exception as e:
        print(f"获取代理API异常:{e}")
        return None


def check_proxy(proxy_info, timeout=8):
    """
    检测代理是否可用
    :param proxy_info: get_one_proxy返回的 {"ip":"xxx","port":"xxx"}
    :param timeout: 超时秒数
    :return: (bool, proxies_dict)  是否可用，requests可用proxies
    """
    if not proxy_info:
        return False, None
    ip = proxy_info["ip"]
    port = proxy_info["port"]
    proxy_str = f"http://{ip}:{port}"
    proxies = {
        "http": proxy_str,
        "https": proxy_str
    }
    try:
        # 测试地址，访问httpbin校验ip
        res = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=timeout)
        if res.status_code == 200:
            return True, proxies
    except Exception:
        pass
    return False, None


def get_usable_proxy(api_url, max_retry=5):
    """
    综合函数：循环获取，直到拿到可用IP
    :param api_url: api地址
    :param max_retry: 最大重试次数
    :return: 可用proxies字典 / None
    """
    for _ in range(max_retry):
        proxy = get_one_proxy(api_url)
        ok, proxies = check_proxy(proxy)
        if ok:
            print(f"✅拿到可用代理 {proxy['ip']}:{proxy['port']}")
            if config.GLOBAL_SESSION:
                config.GLOBAL_SESSION.close()
            sess = requests.Session()
            sess.headers.update({
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Mobile Safari/537.36"
            })
            config.GLOBAL_SESSION = sess
            return proxies
        else:
            print(f"❌代理不可用，继续获取下一个")
    print("⚠️多次尝试没有获取可用代理")
    return None



