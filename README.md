# Central UPI Payment Gateway

This is the term project for BITS F463: Cryptography. It is a simplified implementation of a centralized UPI payment gateway which involves utilising lightweight cryptography in order to speed up essential processes like transactions, using socket programming to facilitate communication between entities, utilising quantum cryptography to expose the vulnerabilities involved in the process and a Front-end React client to perform the various operations.

## Features 

- [Register Merchant](#overview)
- [Register User](#features)
- [Make Payments](#installation)
- [View Transactions (Centralized)](#usage)
- [Generate QR Code](#contributing)


## Operation IDs

- 1: Register Merchant
- 2: Login Merchant
- 3: Register User
- 4: Login User
- 5: User Transaction
- 6: QR Code Generation

## Installation
1. Download the `.zip` file and extract the contents
2. Ensure that npm package manager and python are installed on the system
3. Next run the following commands:
    ```bash
    pip install qiskit qiskit-aer qrcode
    ```
4. Install dependencies for frontend client:
    ```bash
    cd client
    npm install
    npm start
    ```
5. Create virtual environment for the proxy server and install the required libraries
    ```bash
    cd proxy_server
    python -m venv env
    ./env/Scripts/activate 
    pip install -r requirements.txt
    python app.py
    ```
6. On the bank server laptop, run:
    ```bash
    python bank/bank_server.py
    ```
7. On the user and merchant laptops, run:
    ```bash
    python upi_machine/upi_server.py
    ```
8. Now you can perform the operations enabled by the UPI payments gateway

## List of Team Members
- *Bhaskar Ruthvik Bikkina* - *2021A7PS1345H*
- *Neel Saket Racherla* - *2021AAPS1523H*
- *Abhinav Satish* - *2021AAPS1525H*
- *Harikrishna V* - *2021A3PS1662H*
- *Sidharth Saxena* - *2021B4A72488H*

    
