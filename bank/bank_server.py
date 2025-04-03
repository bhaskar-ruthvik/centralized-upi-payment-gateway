import socket			 
import json
from utils import retrieve_from_database, register_user, user_login, get_shaid, register_merchant, merchant_login
import time
available_banks = [
    {
        "bank_name": "HSBC",
        "ifsc_code": "HSBCI000101"
    },
    {
        "bank_name": "HSBC",
        "ifsc_code": "HSBCI000102"
    },
    {
        "bank_name": "HSBC",
        "ifsc_code": "HSBCI000103"
    },
    {
        "bank_name": "ICICI",
        "ifsc_code": "ICICI000201"
    },
    {
        "bank_name": "ICICI",
        "ifsc_code": "ICICI000202"
    },
    {
        "bank_name": "ICICI",
        "ifsc_code": "ICICI00020"
    },
    {
        "bank_name": "SBI",
        "ifsc_code": "SBIIN000301"
    }, 
    {
        "bank_name": "SBI",
        "ifsc_code": "SBIIN000302"
    }, 
    {
        "bank_name": "SBI",
        "ifsc_code": "SBIIN000303"
    }
]

merchants = []
users = []
s = socket.socket()		 
print ("Socket successfully created")
port = 12345			
s.bind(('', port))		 
print ("socket binded to %s" %(port)) 

# put the socket into listening mode 
s.listen(5)	 
print ("socket is listening")		 

# a forever loop until we interrupt it or 
# an error occurs 
while True: 

    # Establish connection with client. 
    c, addr = s.accept()	 
    print ('Got connection from', addr )
    users = retrieve_from_database("database/users.txt")
    merchants = retrieve_from_database("database/merchants.txt")
    # send a thank you message to the client. encoding to send byte type. 
    # c.send("""Hello. This is the bank server. Please choose one of the following operations to proceed with:
    # 1. See List of Banks
    # 2. Exit
    # """.encode()) 

    resp = c.recv(1024).decode()
    #print(resp)
    resp = json.loads(resp.split("\r\n\r")[-1])
    print(resp)
    if resp["id"] == "5":
        c.send(json.dumps({"id":"5"}).encode())
        c.close()
        break
    elif resp["id"] == "1":
        mid = get_shaid([resp["data"]["name"],str(time.time()),resp["data"]["password"]])
        resp["data"]["MID"] = mid 
        register_merchant("database/merchants.txt",json.dumps(resp["data"]))
        c.send(json.dumps({"id": 1, "data": "Registration Complete"}).encode("UTF-8"))
    elif resp["id"] == "2":
        stat = merchant_login(resp["data"]["name"],resp["data"]["password"],merchants)
        if stat == 1:
            c.send(json.dumps({"id": 2, "data": "Login Successful"}).encode())
        else:
            c.send(json.dumps({"id": 2, "data": "Login Failed"}).encode())
    elif resp["id"]=="3":
        uid = get_shaid([resp["data"]["name"],str(time.time()),resp["data"]["password"]])
        mmid = get_shaid([uid, resp["data"]["Mobile Number"]])
        resp["data"]["UID"] = uid
        resp["data"]["MMID"] = mmid
        register_user("database/users.txt",json.dumps(resp["data"]))
        c.send(json.dumps({"id": "3", "data": "Registration Complete"}).encode("UTF-8"))
    elif resp["id"]=="4":
        stat = user_login(resp["data"]["name"],resp["data"]["password"],users)
        if stat == 1:
            c.send(json.dumps({"id": "4", "data": "Login Successful"}).encode())
        else:
            c.send(json.dumps({"id": "4", "data": "Login Failed"}).encode())
    # Close the connection with the client 
    c.close()

