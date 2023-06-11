# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
import json

import requests

url_de = 'http://127.0.0.1:8080/des_decrypt'
url_en = 'http://127.0.0.1:8080/des_encrypt'


def encrypt(password: str):
    resp = requests.post(url=url_en, data=json.dumps({
        'text': password
    }))
    resp = dict(resp.json())
    return resp['res']['encrypted_text']


def decrypt(encrypted_text: bytes):
    resp = requests.post(url=url_de, data=json.dumps({
        'encrypted_text': encrypted_text
    }))
    resp = dict(resp.json())
    return resp['res']['row_text']


if __name__ == '__main__':
    en_text = encrypt('123456abcxyz..')
    print(en_text)
    de_text = decrypt(en_text)
    print(de_text)
