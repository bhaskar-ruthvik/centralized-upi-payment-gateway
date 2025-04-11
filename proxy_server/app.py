from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import socket		
import json	 
from utils import encrypt, decrypt

app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

		

@app.route("/bank_laptop", methods = ["POST"], endpoint = "bank")
@cross_origin()
def index():
    if request.method == "POST":
        port = 12345	
        data = request.json
            
        s = socket.socket()		
        s.connect(('172.20.10.6', port)) 
        s.send(json.dumps(data).encode())
        resp = s.recv(4096).decode()
        print(resp)
        resp = json.loads(resp)
        print(resp)
        s.close()	 
        return jsonify(resp)

@app.route("/user_laptop", methods = ["POST"], endpoint = "user")
@cross_origin()
def index():
    if request.method == "POST":
        port = 3003
        data = request.json

        s = socket.socket()
        s.connect(("127.0.0.1",port))
        # send_msg = {
        #     "id": data["id"]
        # }
        s.send(json.dumps(data).encode())
        resp = s.recv(1024).decode()
        resp = json.loads(resp)
        print(resp)
        s.close()
        return jsonify(resp)

@app.route("/merchant_laptop", methods = ["POST"], endpoint = "merchant")
@cross_origin()
def index():
    if request.method == "POST":
        port = 3003
        data = request.json

        s = socket.socket()
        s.connect(("127.0.0.1",port))
        s.send(json.dumps(data).encode())
        resp = s.recv(1024).decode()
        resp = json.loads(resp)
        print(resp)
        s.close()
        return jsonify(resp)

@app.route("/upi", methods = ["POST"], endpoint = "upimachine")
@cross_origin()
def index():
    if request.method == "POST":
        port = 3003
        data = request.json
        if data["id"]=="5":
            data["data"]["user_data"] = encrypt("This is the key", json.dumps(data["data"]["user_data"]))
        s = socket.socket()
        s.connect(("127.0.0.1",port))
        s.send(json.dumps(data).encode())
        resp = s.recv(1024).decode()
        resp = json.loads(resp)
        print(resp)
        s.close()
        return jsonify(resp)

if __name__ == "__main__":
    app.run(debug=True)
