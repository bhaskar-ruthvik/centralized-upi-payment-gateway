import math
import random
from fractions import Fraction
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.circuit.library import QFT
import random
import re
import json

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 % m0

def generate_rsa_keys(p,q):
    N = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    while gcd(e, phi) != 1:
        e += 2
    d = modinv(e, phi)
    return (e, N), (d, N), (p, q)

def encrypt(message, public_key):
    hex_letters = ["A", "B", "C", "D", "E", "F"]
    e, N = public_key
    cipher = ""
    for digit in message:
        digit = ord(digit)-48
        temp = pow(digit, e, N)
        cipher += str(temp)+random.sample(hex_letters, 1)[0]
    return cipher[:-1]

def decrypt(ciphertext, private_key):
    d, N = private_key
    plain_text = ""
    ciphertext = re.split("[A-F]", ciphertext)
    for digit in ciphertext:
        digit = int(digit)
        temp = pow(digit, d, N)
        plain_text += chr(temp+48)
    return plain_text

'''shors'''
def quantum_period_finding(a: int, N: int) -> int:
    n = math.ceil(math.log2(N))
    m = 2 * n
    qc = QuantumCircuit(m + 1, m)
    qc.x(m)
    qc.h(range(m))
    for q in range(m):
        qc.cp(2 * math.pi * (2**q) / N, q, m)
    qc.append(QFT(m, inverse=True), range(m))
    qc.measure(range(m), range(m))

    simulator = AerSimulator()
    result = simulator.run(transpile(qc, simulator), shots=1024).result()
    counts = result.get_counts()

    for measurement in counts:
        phase = int(measurement, 2) / (2**m)
        frac = Fraction(phase).limit_denominator(N)
        r = frac.denominator
        if pow(a, r, N) == 1:
            return r
    return None

def factor_rsa_modulus(N):
    a = random.randint(2, N-1)
    if math.gcd(a, N) != 1:
        return math.gcd(a, N), N // math.gcd(a, N)

    r = quantum_period_finding(a, N)
    if not r or r % 2 != 0:
        raise Exception("Shor's algorithm failed")

    x = pow(a, r // 2, N)
    factors = [math.gcd(x + 1, N), math.gcd(x - 1, N)]
    for f in factors:
        if 1 < f < N and N % f == 0:
            return f, N // f
    raise Exception("Failed to factor")



if __name__ == "__main__":
    

    users = []
    keys = []
    with open("database/users.txt","r") as f:
        temp_users=  f.read().split("\n")
        users = [json.loads(i) for i in temp_users if i != ""]
        f.close()
    with open("database/keys.txt","r") as f:
        temp_keys = f.read().split("\n")
        keys = [json.loads(i) for i in temp_keys if i != ""]
        f.close()
    pins = []
    uids = []
    for key,user in zip(keys,users):
        pin =  user["PIN"]
        uid = user["UID"]
        print("\nRunning simulated quantum attack using Shor's algorithm...\n")
        while True:
            try:
                public_key = key["public_key"]
                private_key = key["private_key"]
                public_key = tuple(map(int, public_key.replace('(','').replace(')','').split(',')))
                private_key = tuple(map(int, private_key.replace('(','').replace(')','').split(',')))
                p, q = factor_rsa_modulus(public_key[1])
                print(f"Quantum Attack Successful: N = {p} × {q}")
                phi = (p - 1)*(q - 1)
                e = public_key[0]
                d = modinv(e, phi)
                decrypted_pin = decrypt(pin,private_key)
                #print(f"Decrypted PIN using recovered private key: {decrypted_pin}")
                pins.append(decrypted_pin)
                decrypted_uid = decrypt(uid, private_key)
                uids.append(decrypted_uid)
                #print(f"Decrypted UID using recovered private key: {decrypted_uid}")
                break
            except Exception as e:
                print("Quantum attack failed:",e)
                continue
    print("Decrypted PINs: ", pins)
    print("Decrypted UIDs: ", uids)