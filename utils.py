# !/usr/bin/env python3
# _*_ coding: utf-8 _*_
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


class CryptoUtils:
    default_pri_key = b'PriV_KEY'

    @classmethod
    def des_encrypt(cls, text: str, pri_key: bytes = b''):
        """

        :param text: 需要加密的文本字符串
        :param pri_key: 密钥
        用任意的8个字节作为DES的密钥，只要它们满足以下条件：
            每个字节的最低有效位（LSB）是奇偶校验位，也就是说，每个字节中1的个数应该是奇数。
            密钥不是弱密钥或半弱密钥，也就是说，密钥不会导致DES加密或解密时的子密钥相同或互为逆。
        :return encrypted_text: 加密后的字节串
        """
        pri_key = cls.default_pri_key if pri_key in [None, b''] else pri_key
        # 创建一个DES实例，使用ECB模式
        des = DES.new(pri_key, DES.MODE_ECB)
        # 对字符串进行填充，使其长度为8的倍数
        padded_text = pad(text.encode('utf-8'), DES.block_size)
        # 对字符串进行加密，得到字节串
        encrypted_text = des.encrypt(padded_text)

        return encrypted_text

    @classmethod
    def des_decrypt(cls, encrypted_text: bytes, pri_key: bytes = b''):
        """

        :param encrypted_text: 需要解密的字节串
        :param pri_key: 密钥
        :return plain_text: 解密后的原始文本
        """
        pri_key = cls.default_pri_key if pri_key in [None, b''] else pri_key
        des = DES.new(pri_key, DES.MODE_ECB)
        # 对字节串进行解密，得到原始字符串
        plain_text = des.decrypt(encrypted_text)
        # 去除填充，还原字符串
        plain_text = unpad(plain_text, DES.block_size).decode()

        return plain_text
