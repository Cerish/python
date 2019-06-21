#内置时间模块
from datetime import datetime
now = datetime.now()
print(now.timestamp())
# print(now.strftime(%a, %b %d %H:%M))
dt = datetime(2013, 3, 15)
print(dt.timestamp())
t = 1564651311.0
print(datetime.fromtimestamp(t))

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)