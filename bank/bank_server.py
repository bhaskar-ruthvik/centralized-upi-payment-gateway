import socket			 
import json
from utils import *
import time
available_banks = [
    {
        "bank_name": "HDFC",
        "ifsc_code": "HDFCI000101"
    },
    {
        "bank_name": "HDFC",
        "ifsc_code": "HDFCI000102"
    },
    {
        "bank_name": "HDFC",
        "ifsc_code": "HDFCI000103"
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
ledger = read_ledger("database/chain_ledger.json")
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
    if resp["id"] == "10":
        c.send(json.dumps({"id":"10"}).encode())
        c.close()
        break
    elif resp["id"] == "1":
        mid = get_shaid([resp["data"]["name"],str(time.time()),resp["data"]["password"]])
        resp["data"]["MID"] = mid 
        register_merchant("database/merchants.txt",json.dumps(resp["data"]))
        c.send(json.dumps({"id": 1, "data": "Registration Complete"}).encode("UTF-8"))
    elif resp["id"] == "2": # Not a useful operation as login is not required
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
    elif resp["id"]=="4": # Not a useful operation as login is not required
        stat = user_login(resp["data"]["name"],resp["data"]["password"],users)
        if stat == 1:
            c.send(json.dumps({"id": "4", "data": "Login Successful"}).encode())
        else:
            c.send(json.dumps({"id": "4", "data": "Login Failed"}).encode())
    elif resp["id"]=="5":
        # Decrypt the user information
        user_data = json.loads(decrypt("This is the key",resp["data"]["user_data"]))
        print(user_data)
        # Validate all the user information
        merchant_valid, merchant = validate_merchant(resp["data"]["MID"],merchants)
        print("Merchant Valid: ", merchant_valid)
        print(merchant)
        if merchant_valid == 1:
            user_valid, user = validate_user(user_data, users)
            print("User Valid: ", user_valid)
            if user_valid == 1:
                merchant["Amount in Account"] = str(float(merchant["Amount in Account"]) + float(user_data["Amount"]))
                # Add to Blockchain if the transaction is successful
                transaction = create_transaction_block(user["UID"], resp["data"]["MID"], user_data["Amount"])
                add_transaction(ledger, transaction)
                write_to_ledger(ledger, "database/chain_ledger.json")
                update_amount_in_db(merchant["MID"],merchant["Amount in Account"],merchants)
                write_to_db("database/users.txt",users)
                write_to_db("database/merchants.txt",merchants)
                print("Success")
                c.send(json.dumps({"id": "5", "data": "Transaction Successful"}).encode())
            else:
                print("Fail")
                c.send(json.dumps({"id": "5", "data": "Transaction Failed"}).encode())
    elif resp["id"]=="7":
        data = {}
        with open("database/chain_ledger.json","r") as f:
            data = json.loads(f.read())
        
        c.send(json.dumps({"id": "7", "data": data}).encode())

    
        # Send the status back to UPI machine
    # Close the connection with the client 
    c.close()

