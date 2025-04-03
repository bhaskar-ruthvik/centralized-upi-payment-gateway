import socket			 
import json
from utils import retrieve_from_database, register_user, user_login, get_shaid
import time
s = socket.socket()		 
port = 3002			
s.bind(('', port))		 
s.listen(5)	 
print ("socket is listening")		 

merchants = []

while True: 

    c, addr = s.accept()	 
    print ('Got connection from', addr )

    merchants = retrieve_from_database("database/users.txt")
    # c.send("""Hello. This is the bank server. Please choose one of the following operations to proceed with:
    # 1. Register
    # 2. Login
    # 3. Make Payment
    # 4. Exit
    # """.encode()) 

    resp = json.loads(c.recv(1024).decode())
    #.split("\r\n\r")[-1]
    print(resp)
    if resp["id"] == "4":
        c.send(json.dumps({"id":2}).encode())
        c.close()
        break
    elif resp["id"] == "2":
        stat = user_login(resp["data"]["name"],resp["data"]["password"],merchants)
        if stat == 1:
            c.send(json.dumps({"id": 2, "data": "Login Successful"}).encode())
        else:
            c.send(json.dumps({"id": 2, "data": "Login Failed"}).encode())
    elif resp["id"] == "1":
        uid = get_shaid([resp["data"]["name"],str(time.time()),resp["data"]["password"]])
        mmid = get_shaid([uid, resp["data"]["Mobile Number"]])
        resp["data"]["UID"] = uid
        resp["data"]["MMID"] = mmid
        register_user("database/users.txt",json.dumps(resp["data"]))
        c.send(json.dumps({"id": 1, "data": "Registration Complete"}).encode("UTF-8"))
    c.close()

