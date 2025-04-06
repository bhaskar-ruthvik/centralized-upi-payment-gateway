import socket
import hashlib
import json
import time

def get_shaid(raw_values):
    h = hashlib.sha256()
    temp = ""
    for value in raw_values[:-1]:
        temp+=value
        temp+="\n"
    temp+=raw_values[-1]
    h.update(temp.encode("UTF-8"))
    return h.hexdigest()[:16]

def get_shaid_full(raw_values):
    h = hashlib.sha256()
    temp = ""
    for value in raw_values[:-1]:
        temp+=value
        temp+="\n"
    temp+=raw_values[-1]
    h.update(temp.encode("UTF-8"))
    return h.hexdigest()


def retrieve_from_database(dbpath):
    with open(dbpath, "r") as f:
        blob = f.read()
    return blob.split("\n")
    
def register_user(dbpath,merchant_data): 
    with open(dbpath, "a") as f:
        f.write("\n"+merchant_data)

def user_login(name,password, users):
    for user in users:
        user = json.loads(user)
        if name == user["name"] and password == user["password"]:
            return 1
    return 0

    
def register_merchant(dbpath,merchant_data): 
    with open(dbpath, "a") as f:
        f.write("\n"+merchant_data)

def merchant_login(name,password, users):
    for user in users:
        user = json.loads(user)
        if name == user["name"] and password == user["password"]:
            return 1
    return 0

def decrypt_hashdata(hash_data):
 
    return hash_data

def validate_user(user_data, users):
    for idx, user in enumerate(users):
        user = json.loads(user)
        if user["MMID"] == user_data["MMID"]:
            if user["PIN"] == user_data["PIN"]:
                if float(user_data["Amount"]) <= float(user["Amount in Account"]):
                    user["Amount in Account"] = str(float(user["Amount in Account"]) - float(user_data["Amount"]))
                    users[idx] = json.dumps(user)
                    return 1, user

    return 0, None

def validate_merchant(MID, merchants):
    for merchant in merchants:
        merchant = json.loads(merchant)
        if merchant["MID"] == MID:
            return 1, merchant 
    return 0, None


def read_ledger(dbpath):
    with open(dbpath, "r") as f:
        ledger = json.loads(f.read())
    return ledger

def create_transaction_block(UID, MID, Amount):
    block_hash = get_shaid_full([UID, MID, str(time.time()), str(Amount)])
    transaction = {
        "block_hash": block_hash,
        "previous_hash": 64*"0",
        "timestamp": time.time()
    }
    return transaction

def add_transaction(ledger, transaction):
    if len(ledger["transactions"]) > 1:
        transaction["previous_hash"] = ledger["transactions"][-1]["block_hash"] 
    ledger["transactions"].append(transaction)

def write_to_ledger(ledger, dbpath):
    with open(dbpath, "w") as f:
        f.write(json.dumps(ledger))

def update_amount_in_db(MID,amount,merchants):
    for indx, merchant in enumerate(merchants):
        merchant = json.loads(merchant)
        if merchant["MID"]== MID:
            merchant["Amount in Account"] = amount
            print("Merchant Updated: ", json.dumps(merchant))
            merchants[indx] = json.dumps(merchant)
        
def write_to_db(dbpath,merchants): 
    with open(dbpath, "w") as f:
        f.write("\n".join(merchants))

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

