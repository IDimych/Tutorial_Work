#import urllib2
#import urllib.request

#url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
#response = urllib.request.urlopen(url)
#webContent = response.read()

#print(webContent[0:300])


import urllib.request
url='http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
response = urllib.request.urlopen(url)
print(response.read().decode())
