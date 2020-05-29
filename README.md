# Cryptanalysis of Encryption Schemes
This repo is created to host examples of cracking popular encryption schemes which have known weaknesses.

# Requirements
You will need Python 3 and the `pycryptodome` module.

# Exploits
## AES in MODE_CTR
The popular AES symmetric encryption scheme offers the ability to encrypt/decrypt data streams instead of blocks of data with padding.

If not properly implemented, the cipher is relatively easy to crack.

For this exploit, we assume that:
1. The attacker can submit (or guess) a string of plaintext provided as input for the encryption, and can see the resulting ciphertext.
2. The attacker can see other ciphertext produced by the system but not the plaintext
3. The attacker does not have access to the symmetric key.

If the MODE_CTR scheme is not properly implemented, it can result in the attacker being able to decrypt ciphertext produced by the system without knowing what the key is!

Take a look at [aes_modeCTR.py](./aes_modeCTR.py) for a working exploit. Can you figure out what the vulnerability is? Bonus points if you can explain how this affected [WEP](https://en.wikipedia.org/wiki/Wired_Equivalent_Privacy) encryption.


