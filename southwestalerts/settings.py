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

# Find all USERNAME# / PASSWORD# pairs and add the to the list of users to check
#_index = 1
users = []
#while os.environ.get('USERNAME{}'.format(_index)):
#    user = User(os.environ['USERNAME{}'.format(_index)], os.environ['PASSWORD{}'.format(_index)], None)
#    users.append(user)
#    _index += 1
for k, v in json.load(open('accounts.json')).items():
    users.append(User(str(k),str(v),None))
