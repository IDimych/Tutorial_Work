import urllib.request
import json
import datetime
import csv

FILENAME = "accounts.csv"

url = 'https://etc.2miners.com/api/accounts/0xc53a2409ef3c57eeab564b8a3d66d64ccc027cda'
response = urllib.request.urlopen(url)
accounts = json.loads(response.read())

print(accounts)
print("===================================")

curDateTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
newAccounts = dict()

# TODO Сделать заголовки, один раз вводишь в словарь, потом их использовать, вроде словать заголовков
newAccounts["DateTime"] = curDateTime
newAccounts["24hnumreward"] = accounts["24hnumreward"]
newAccounts["24hreward"] = accounts["24hreward"]
newAccounts["currentHashrate"] = accounts["currentHashrate"]
newAccounts["hashrate"] = accounts["hashrate"]


# TODO Сделать добавление строк, а не перезапись
with open(FILENAME, "a", newline="") as file:
    columns = ["DateTime", "24hnumreward","24hreward","currentHashrate","hashrate"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    writer.writerow(newAccounts)

print(newAccounts)
print("===================================")
