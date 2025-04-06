import time
import qrcode
import os

ALPHA = 8
BETA = 3
WORD_SIZE = 64
MASK = 0xFFFFFFFFFFFFFFFF
ROUNDS = 32
def ROR(x,r):
    return ((x >> r) | (x << (WORD_SIZE - r))) & MASK

def ROL(x,r):
    return ((x << r) | (x >> (WORD_SIZE - r))) & MASK

def expand_keys(key):
    
    k = [key[0]]
    l = key[1:]
    for i in range(ROUNDS - 1): 
        new_l = (ROR(l[i],ALPHA)+k[i])& MASK
        new_l ^= i
        k.append(new_l ^ ROL(k[i],BETA))
        l.append(new_l)
    return k
def speck_encrypt(plaintext, expanded_keys):
    x, y = plaintext[:16], plaintext[16:]
    x, y = int(x,16), int(y,16)
    for key in expanded_keys:
        x = (ROR(x, ALPHA) + y) & MASK
        x ^= key
        y = ROL(y, BETA) ^ x
    return hex(x)[2:]+hex(y)[2:]

def speck_decrypt(ciphertext, expanded_keys):
    x, y = ciphertext[:16], ciphertext[16:]
    x, y = int(x,16), int(y,16)
    reverse_keys = reversed(expanded_keys)
    for key in reverse_keys:
        y = (ROR(y ^ x, BETA) & MASK)
        x ^= key
        x = (x-y) & MASK
        x = (ROL(x, ALPHA)) & MASK
    return hex(x)[2:]+hex(y)[2:]

def pad_string(s):
    while len(s) < 16:
        s = '0' + s
    return s
def generate_qr_code(data,MID):
    qr = qrcode.QRCode()
    qr.add_data(data)
    img = qr.make_image(fill_color="black", back_color="white")

    name = str(int(time.time()))
    if not os.path.exists("client/public/qrs/"+MID):
        os.makedirs("client/public/qrs"+"/"+MID)
    img.save(f"client/public/qrs/{MID}/{name}.png")
    return name  



# plaintext = f"31788189cb7b5cbe"
# timestamp_hex = hex(int(time.time()))[2:]
# padded_timestamp_hex = pad_string(timestamp_hex)
# plaintext += padded_timestamp_hex
# key = [0x1918234A1110B364, 0x090876AB0100ABCD] # Dummy Key
# round_keys = expand_keys(key)
# ciphertext = speck_encrypt(plaintext, round_keys)
# generate_qr_code(ciphertext, plaintext[:16])
# print("Plaintext: ", plaintext)
# print("Ciphertext: ", ciphertext)
# decrypted = speck_decrypt(ciphertext, round_keys)


# print("Decrypted: ", decrypted)