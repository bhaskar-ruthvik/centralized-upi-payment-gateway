import socket			 
import json
from utils import decrypt_vmid
import time
s = socket.socket()
t = socket.socket()		 
port = 3003	
bank_port = 12345		
s.bind(('', port))		 
s.listen(5)	 
print ("socket is listening")		 

merchants = []

while True: 

    c, addr = s.accept()	 
    print ('Got connection from', addr )

    resp = json.loads(c.recv(1024).decode())
    #.split("\r\n\r")[-1]
    print(resp)
    if resp["id"] == "5":
        t = socket.socket()
        t.connect(('127.0.0.1', bank_port))
        # Decrypt the VMID and send the hashed user details to the bank server
        resp["data"]["MID"] = decrypt_vmid(resp["data"]["VMID"])
        t.send(json.dumps(resp).encode())
        resp = t.recv(1024).decode()
        resp = json.loads(resp)
        print(resp)
        # Send Status back to user
        c.send(json.dumps(resp).encode())
        t.close()
    c.close()

