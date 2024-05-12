from datetime import datetime

n=int(input())

class Data:
    def __init__(self,date,dow,weather):
        self.date=date
        self.dow=dow
        self.weather=weather

data_list=list()
recent_date="3000-12-31"
recent_index=-1
for i in range(n):
    date,dow,weather=map(str,input().split())
    data_list.append(Data(date,dow,weather))
    a=datetime(int(recent_date[0:4]),int(recent_date[5:7]),int(recent_date[8:]))
    b=datetime(int(date[0:4]),int(date[5:7]),int(date[8:]))
    if a>b and weather=="Rain":
        recent_date=date
        recent_index=i

print(data_list[recent_index].date,data_list[recent_index].dow,data_list[recent_index].weather)