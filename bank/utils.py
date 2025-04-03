import socket
import hashlib
import json

def get_shaid(raw_values):
    h = hashlib.sha256()
    temp = ""
    for value in raw_values[:-1]:
        temp+=value
        temp+="\n"
    temp+=raw_values[-1]
    h.update(temp.encode("UTF-8"))
    return h.hexdigest()[:16]


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