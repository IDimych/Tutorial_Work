#https://golos.io/ru--programmirovanie/@pythono/uroki-python-12-rabotaem-s-internetom
# Уроки Python - 12 Работаем с интернетом
#---------------------------------------
# Код не работает
import requests
s=requests.get('https://m.news.yandex.ru')
print(s.text)

#import requests
#user_id = 12345
#url = 'http://www.kinopoisk.ru/user/%d/votes/list/ord/date/page/2/#list' % (user_id) # url для второй страницы
#r = requests.get(url)
#with open('test.html', 'w') as output_file:
#  output_file.write(r.text.encode('utf8'))