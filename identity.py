import config
import os
import json

def identity(name,idcard):

    # # 拼接完整路径
    # full_pic1 = os.path.join(folder_path, pic1_name)
    # full_pic2 = os.path.join(folder_path, pic2_name)
    #
    # url = "https://6g1.gjjzzx.online/api/v1/user/identity"
    #
    # files = {
    #     "front": (pic1_name, open(full_pic1, "rb"), "image/jpeg"),
    #     "back": (pic2_name, open(full_pic2, "rb"), "image/jpeg")
    # }
    #
    # data = {
    #     "realName": info_dict.get("realName"),
    #     "idNumber": info_dict.get("idNumber"),
    # }
    # try:
    #     resp = config.GLOBAL_SESSION.put(url, data=data, files=files, proxies=config.PROXY)
    #     print(resp.json())
    # finally:
    #     files["front"][1].close()
    #     files["back"][1].close()
    url = "https://www.ceic.cam/member/realsave.shtml"
    data = {
        "realname":name,
        "idcard":idcard
    }
    resp = config.GLOBAL_SESSION.post(url, json=data,proxies=config.PROXY)
    print(resp.json())


