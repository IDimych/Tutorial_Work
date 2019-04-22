#import urllib2
#import urllib.request

#url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
#response = urllib.request.urlopen(url)
#webContent = response.read()

#print(webContent[0:300])


import urllib.request
url='https://etc.2miners.com/ru/account/0xc53a2409ef3c57eeab564b8a3d66d64ccc027cda#rewards-tab'
response = urllib.request.urlopen(url)
webContent = response.read().decode('utf8')
print(webContent)

f = open('etc_2miners.html', 'w', encoding='UTF8')
f.write(webContent)
f.close()

#print(webContent.decode())
