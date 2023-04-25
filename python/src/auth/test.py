import datetime
import os
import jwt
from flask import Flask, request
from flask_mysqldb import MySQL



server = Flask(__name__)
mysql = MySQL(server)

# config
server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")

print("hello")

if __name__ == "__main__": #when we run this file
    print("hello2")
    print(__name__)
    server.run(host="0.0.0.0", port=5000) #docker container에서 돌리면 이 서버는 자신의 IP를 받게되므로, 모든 IP에게서 듣는걸로 설정
    print("auth server is running on port : 5000")