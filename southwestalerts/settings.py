import os
import json

class User:
    username = None
    password = None
    headers = None

    def __init__(self, username, password, headers):
        self.username = username
        self.password = password
        self.headers = headers

users = []
for k, v in json.load(open('accounts.json')).items():
    users.append(User(str(k),str(v),None))
