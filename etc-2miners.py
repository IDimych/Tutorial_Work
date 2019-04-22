import urllib.request
import json
import datetime

url = 'https://etc.2miners.com/api/accounts/0xc53a2409ef3c57eeab564b8a3d66d64ccc027cda'
response = urllib.request.urlopen(url)
accounts = response.read().decode()
print(accounts)

print("loads(accounts)")
x = json.loads(accounts)
n = dict()
n["DateTime"]=datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
n.update(x)

print(n)

with open("etc_2miners_accounts.json", "a") as write_file:
    json.dump(n, write_file)

print("dumps(accounts)")
d = json.dumps(accounts)
print(d)
