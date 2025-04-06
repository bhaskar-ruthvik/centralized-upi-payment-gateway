def encrypt(key, plaintext):
    idx = 0
    while len(key) < len(plaintext):
        key += key[idx % len(key)]
        idx+=1
    
    string = ""
    for i in range(len(plaintext)):
        string += chr(ord(plaintext[i]) ^ ord(key[i]))
    return string

def decrypt(key, ciphertext):
    idx = 0
    while len(key) < len(ciphertext):
        key += key[idx % len(key)]
        idx+=1
    
    string = ""
    for i in range(len(ciphertext)):
        string += chr(ord(ciphertext[i]) ^ ord(key[i]))
    return string

