#!/usr/bin/python
# Output Date+Time
import datetime

print ("===================")
print ("Current Date + Time")
print ("===================")

now = datetime.datetime.now()
day = now.day
month = now.month
year = now.year

print (now.strftime("%d-%m-%Y %H:%M"))