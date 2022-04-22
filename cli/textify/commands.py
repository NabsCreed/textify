
import requests

SERVER_URL = "https://api.textify.io"

ID = 'abd7910102'
def Pull():
    r = requests.get(SERVER_URL + '/pull/' + ID)
    if r.status_code == 200:
        print("Success")
    else:
        print("Failed!!!")
def Push(payload):
    r = requests.post(SERVER_URL + '/push/' + ID, data = payload )



