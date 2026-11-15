import hashlib
import random
import re
import time
import random
from datetime import datetime, timedelta


def random_phone() -> str:
    # 国内主流手机号段
    prefix_list = [
        130,131,132,133,134,135,136,137,138,139,
        144,145,147,149,
        150,151,152,153,155,156,157,158,159,
        162,165,166,167,
        170,171,172,173,175,176,177,178,
        180,181,182,183,184,185,186,187,188,189,
        190,191,192,193,195,196,197,198,199
    ]
    prefix = random.choice(prefix_list)
    suffix = random.randint(0, 99999999)
    return f"{prefix}{suffix:08d}"

first_names = ["王","李","张","刘","陈","杨","黄","赵","吴","周","徐","孙","胡","朱","高","林","何","郭","马","罗"]
last_names = ["伟","芳","娜","秀英","敏","静","丽","强","磊","军","洋","勇","艳","杰","娟","涛","明","超","秀兰","霞","平","刚","桂英","文","华","玲","辉","鑫","鹏","宇"]

def random_true_name() -> str:
    """随机生成中文姓名，适配true_name字段"""
    surname = random.choice(first_names)
    given = random.choice(last_names)
    # 二字名 / 三字名随机
    if random.random() > 0.4:
        given2 = random.choice(last_names)
        return surname + given + given2
    else:
        return surname + given



def generate_device_info():
    # 生成时间戳部分
    ts = int(time.time() * 1000)
    # 随机字符串
    rand_str = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=7))
    device_code = f"h5-{ts}-{rand_str}"

    # 根据deviceCode生成设备指纹（sha256）
    fp_bytes = device_code.encode("utf-8")
    device_fingerprint = hashlib.sha256(fp_bytes).hexdigest()

    return device_code, device_fingerprint

def generate_fake_id() -> str:
    """生成一个格式合法的虚拟身份证号，仅用于本地测试。"""

    weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_map = "10X98765432"

    area = f"{random.randint(100000, 999999)}"

    start = datetime(1960, 1, 1)
    end = datetime(2005, 12, 31)
    birth = start + timedelta(days=random.randint(0, (end - start).days))
    birth_str = birth.strftime("%Y%m%d")

    sequence = f"{random.randint(0, 999):03d}"

    id17 = f"{area}{birth_str}{sequence}"
    check = check_map[sum(int(a) * b for a, b in zip(id17, weights)) % 11]
    return id17 + check