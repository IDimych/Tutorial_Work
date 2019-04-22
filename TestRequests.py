#import urllib.request
#response = urllib.request.urlopen('https://httpbin.org/get')
#print(response.read().decode())

#import requests
#req = requests.get('https://tutsplus.com/')

#from urllib.request import urlopen

#resp = urlopen('http://ya.ru')
#print(resp.info())  # headers
#print(resp.read())  # data

#my_file = open('ya.txt', 'w', encoding='utf8')
#my_file.write(resp.read().decode('utf8'))
#print(resp.read().decode('utf8'))

#my_file.close()

import requests
responce = requests.get('https://ya.ru')
print(responce.text)

