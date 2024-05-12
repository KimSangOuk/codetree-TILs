from datetime import datetime

n=int(input())

class Data:
    def __init__(self,date,dow,weather):
        self.date=date
        self.dow=dow
        self.weather=weather

data_list=list()
recent_date="2101-12-31"
recent_index=-1
for i in range(n):
    date,dow,weather=map(str,input().split())
    a=datetime(int(recent_date[0:4]),int(recent_date[5:7]),int(recent_date[8:]))
    b=datetime(int(date[0:4]),int(date[5:7]),int(date[8:]))
    if a<b and weather=="Rain":
        recent_date=date
        recent_index=i

print(data_list[i].date,data_list[i].dow,data_list[i].weather)