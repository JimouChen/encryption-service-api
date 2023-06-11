# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
import base64

from fastapi import FastAPI, Request
from utils import CryptoUtils

app = FastAPI()


@app.post("/des_encrypt")
async def des_encrypt(request: Request):
    data = await request.json()
    text = data.get('text')
    pri_key = data.get('pri_key')
    encrypted_text: bytes = CryptoUtils.des_encrypt(text, pri_key)
    return {
        'res': {
            "code": 200,
            "status": "OK",
            "encrypted_text": base64.b64encode(encrypted_text).decode()
        }
    }


@app.post("/des_decrypt")
async def des_encrypt(request: Request):
    data = await request.json()
    encrypted_text = data.get('encrypted_text').encode()
    encrypted_text = base64.b64decode(encrypted_text)
    pri_key = data.get('pri_key')
    row_text = CryptoUtils.des_decrypt(encrypted_text, pri_key)
    return {
        'res': {
            "code": 200,
            "status": "OK",
            "row_text": row_text
        }
    }
