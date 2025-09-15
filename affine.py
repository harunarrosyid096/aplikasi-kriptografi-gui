# affine.py

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("Modular inverse does not exist")

def affine_encrypt(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("'a' must be coprime with 26")
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr(((a * (ord(char) - base) + b) % 26) + base)
        else:
            result += char
    return result

def affine_decrypt(cipher, a, b):
    a_inv = mod_inverse(a, 26)
    result = ''
    for char in cipher:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr(((a_inv * ((ord(char) - base) - b)) % 26) + base)
        else:
            result += char
    return result

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a