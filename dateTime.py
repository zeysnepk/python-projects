#A module is used for time and date operations
from datetime import datetime

print(datetime.now())
print(datetime.now().year)

print("\n")

now = datetime.now()
print(now.year)
print(now.month)
print(now.day)

print("\n")

#ctime()
print(datetime.ctime(now))

print("\n")


#strftime()
#  %Y --> Year info
#  %B --> Month name
#  %A --> Day name
#  %X --> Time info
#  %D --> Day info

print(datetime.strftime(now,"%Y"))
print(datetime.strftime(now,"%B"))
print(datetime.strftime(now,"%A"))
print(datetime.strftime(now,"%X"))
print(datetime.strftime(now,"%D"))
print(datetime.strftime(now,"%B %Y"))

print("\n")

#timestamp() / fromtimestamp()
second = datetime.timestamp(now) #converts date to second
print(second)

date = datetime.fromtimestamp(second) #converts second to date
print(date)

print(datetime.fromtimestamp(0)) 


#date setting
setDate = datetime(2004,5,21)

print(now - setDate)