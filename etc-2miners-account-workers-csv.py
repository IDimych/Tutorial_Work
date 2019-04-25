import urllib.request
import json
import datetime
import csv
import os

url = 'https://etc.2miners.com/api/accounts/0xc53a2409ef3c57eeab564b8a3d66d64ccc027cda'
response = urllib.request.urlopen(url)
accounts = json.loads(response.read())

print(accounts)
print("===================================")

print("----------------------")
print(accounts["workers"])
print("----------------------")
# TODO Пройтись по словарю, выделить вокеры и считать данные каждого


curDateTime = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
# Получить имя файла
fileName = datetime.datetime.now().strftime("%d-%m-%Y")+"_workers.csv"
# Проверить, есть ли файл, если есть, пишем в него, если нет, то создаем новый с полями
if not os.path.isfile(fileName):
    print("Файла нет!")
    with open(fileName, "a", newline="") as file:
        columns = ["DateTime", "24hnumreward", "24hreward", "currentHashrate", "hashrate","paymentsTotal","roundShares","workersOffline","workersOnline","workersTotal"]
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()

newWorkers = dict()

# TODO Сделать заголовки, один раз вводишь в словарь, потом их использовать, вроде словать заголовков
newWorkers["DateTime"] = curDateTime

# TODO Сделать добавление строк, а не перезапись, но чтобы при добавлении, добавлялись данные, поля должны добавлять для нового файла
with open(fileName, "+a", newline="") as file:
    columns = ["DateTime", "24hnumreward", "24hreward", "currentHashrate", "hashrate", "paymentsTotal", "roundShares",
               "workersOffline", "workersOnline", "workersTotal"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writerow(newWorkers)

print(newWorkers)
print("===================================")
