import socket		
import json	 
port = 12345			

while True:
    s = socket.socket()		
    s.connect(('127.0.0.1', port)) 

    print (s.recv(1024).decode())
    send_msg = input("Enter Your Response: ")
    s.send(send_msg.encode())
    resp = s.recv(1024).decode()
    resp = json.loads(resp)
    print(resp)
    if resp["id"] == "2":
        break
    
    s.close()	 
	