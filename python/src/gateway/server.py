import os, gridfs, pika, json
from flask import Flask, request
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import util

print(__name__)
server = Flask(__name__)
server.config["MONGODB"]