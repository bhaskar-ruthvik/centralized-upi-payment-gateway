import socket			 
import json
from utils import decrypt_vmid
import time
from speck import *

s = socket.socket()
t = socket.socket()		 
port = 3003	
bank_port = 12345		
s.bind(('', port))		 
s.listen(5)	 
print ("socket is listening")		 

merchants = []
key = [0x1918234A1110B364, 0x090876AB0100ABCD]
round_keys = expand_keys(key)
while True: 

    c, addr = s.accept()	 
    print ('Got connection from', addr )

    resp = json.loads(c.recv(1024).decode())
    #.split("\r\n\r")[-1]
    print(resp)
    if resp["id"] == "5":
        t = socket.socket()
        t.connect(('172.20.10.6', bank_port))
        # Decrypt the VMID and send the hashed user details to the bank server
        mid = speck_decrypt(resp["data"]["VMID"],round_keys)
        print("Decrypted MID: ", mid)
        resp["data"]["MID"] = mid[:16]
        t.send(json.dumps(resp).encode())
        resp = t.recv(1024).decode()
        resp = json.loads(resp)
        print(resp)
        # Send Status back to user
        c.send(json.dumps(resp).encode())
        t.close()
    elif resp["id"]=="6":
        mid = resp["data"]["MID"]
        print(mid)
        padded_timestamp_hex = pad_string(hex(int(time.time()))[2:])
        plaintext = mid + padded_timestamp_hex
        ciphertext = speck_encrypt(plaintext, round_keys)
        file_name = generate_qr_code(ciphertext, mid)
        c.send(json.dumps({"id": "6","data": { "status": "QR Generated Successfully", "file_name": file_name}}).encode())
    elif resp["id"]=="1"  or resp["id"]=="3":
        t = socket.socket()
        t.connect(('172.20.10.6', bank_port))
        t.send(json.dumps(resp).encode())
        resp = t.recv(1024).decode()
        resp = json.loads(resp)
        print(resp)
        c.send(json.dumps(resp).encode())
        t.close()
    c.close()

