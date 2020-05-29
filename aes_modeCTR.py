from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes

KEY = "8@#e7aschj2bd7a!dh83s3Sz".encode('utf8')
nonce=SHA256.new(KEY).digest()[:12]

def xor(bytes1, bytes2):
    return hex( int(bytes1.hex(),16) ^ int(bytes2.hex(),16) )

def decrypt(e):
    cipher = AES.new(KEY, AES.MODE_CTR, nonce=nonce)
    plaintext = cipher.decrypt(e)
    return plaintext

def encrypt(data):
    cipher = AES.new(KEY, AES.MODE_CTR, nonce=nonce)
    ciphertext = cipher.encrypt(data)
    return ciphertext

def crack(Cx, Cy, Cz, Px):
    if len(Cx) == len(Cy):
        ciphertextXor = xor(Cx, Cz)
        Pc = xor(bytes.fromhex(ciphertextXor[2:]), Px)
        Pc_ = bytes.fromhex(Pc[2:]).decode('utf-8')
        print('Decrypted text from Cz:', Pc_)
    else:
        print('The provided ciphertexts must have the same length, to exploit key reuse for AES MODE_CTR')


Px = 'This is a secret sentence'.encode('ascii')
Py = 'This is secret number two'.encode('ascii')

Cx = encrypt(Px)
Cy = encrypt(Py)
Cz = b'\x83W\x11\x80\x87\x0e\xad\xcb?\x03v0\xd4\x00\xc6*5\xc0\x8b\x97\xc8\x1bh\xd1\xa9'

print('Ciphertext from Px:', Cx.hex())
print('Ciphertext from Py:', Cy.hex())
print('Ciphertext from unknown plaintext Cz:', Cz.hex())

Px_ = decrypt(Cx)
Py_ = decrypt(Cy)

print('Decrypted text Px_:', bytes.fromhex(Px_.hex()).decode('utf-8'))
print('Decrypted text Py_:', bytes.fromhex(Py_.hex()).decode('utf-8'))

crack(Cx, Cy, Cz, Px)
