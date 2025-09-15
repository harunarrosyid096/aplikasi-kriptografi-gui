# aes_custom.py

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def aes_encrypt(plain_text, key):
    key = key.encode('utf-8')[:16].ljust(16, b'0')
    cipher = AES.new(key, AES.MODE_ECB)
    ct_bytes = cipher.encrypt(pad(plain_text.encode(), 16))
    return base64.b64encode(ct_bytes).decode('utf-8')

def aes_decrypt(cipher_text, key):
    key = key.encode('utf-8')[:16].ljust(16, b'0')
    cipher = AES.new(key, AES.MODE_ECB)
    pt = unpad(cipher.decrypt(base64.b64decode(cipher_text)), 16)
    return pt.decode('utf-8')