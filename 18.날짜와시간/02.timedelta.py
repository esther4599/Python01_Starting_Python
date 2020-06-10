import datetime
d_100 = datetime.timedelta(days=100) # 100 days, 0:00:00
print(d_100)

print(datetime.datetime.now() + d_100) # 2020-09-18 23:36:38.343693
print(type(datetime.datetime.now())) #<class 'datetime.datetime'>

# +, -연산 모두 지원
bd_100 = datetime.timedelta(days=-100)
print(datetime.datetime.now() + bd_100) # 2020-03-02 23:38:18.389285
print(datetime.datetime.now() - d_100) # 2020-03-02 23:39:08.629384

tomorrow = datetime.datetime.now().replace(hour=9, minute=0, second=0) \
           + datetime.timedelta(days=1)
print(tomorrow) # 2020-06-11 09:00:00.920766

#아래는 실습 : 출력 형식 지정
hundred_after = datetime.datetime.now().replace(hour=9, minute=0, second=0) + datetime.timedelta(days=100)
print("{}/{}/{}  {}:{}:{}"
      .format(hundred_after.year,hundred_after.month, hundred_after.day,
              hundred_after.hour, hundred_after.minute, hundred_after.second))