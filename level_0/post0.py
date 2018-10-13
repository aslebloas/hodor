#!/usr/bin/python3
import requests

url = 'http://158.69.76.135/level0.php'
values = {'id': '377', 'holdthedoor': 'Submit'}

for i in range(1024):
    r = requests.post(url, data=values)

print(r.status_code, r.reason)
