# vigenere.py

def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return ''.join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def vigenere_encrypt(plain_text, key):
    key = generate_key(plain_text, key)
    cipher_text = ''
    for p, k in zip(plain_text, key):
        if p.isalpha():
            shift = (ord(p.upper()) + ord(k.upper()) - 2 * ord('A')) % 26
            cipher_text += chr(shift + ord('A')) if p.isupper() else chr(shift + ord('a'))
        else:
            cipher_text += p
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    key = generate_key(cipher_text, key)
    plain_text = ''
    for c, k in zip(cipher_text, key):
        if c.isalpha():
            shift = (ord(c.upper()) - ord(k.upper()) + 26) % 26
            plain_text += chr(shift + ord('A')) if c.isupper() else chr(shift + ord('a'))
        else:
            plain_text += c
    return plain_text

