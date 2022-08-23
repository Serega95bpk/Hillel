import datetime

now = datetime.datetime.now()

year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day

print(year(now))
print(month(now))
print(day(now))
