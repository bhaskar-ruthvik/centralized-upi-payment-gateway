import socket		
import json	
from utils import get_shaid
import time
port = 3001			

while True:
    s = socket.socket()		
    s.connect(('127.0.0.1', port)) 

    print (s.recv(1024).decode())
    op_id = input("Enter Your Response: ")

    send_msg = {
        "id": op_id
    }
    if op_id == "1":
        name = input("Name: ")
        password = input("Password: ")
        ifsc_code = input("IFSC Code: ")
        amount_in_acc = input("Amount: ")
        send_msg["data"] = {
            "name": name,
            "password": password,
            "IFSC Code": ifsc_code,
            "Amount in Account": amount_in_acc,
            "MID": get_shaid([name,str(time.time()),password])
        }
    elif op_id == "2":
        name = input("Name: ")
        password = input("Password: ")
        send_msg["data"] = {
            "name": name,
            "password": password
        }
    s.send(json.dumps(send_msg).encode())

    resp = s.recv(1024).decode()
    resp = json.loads(resp)
    print(resp)
    if resp["id"] == "2":
        break
    
    s.close()	 
	