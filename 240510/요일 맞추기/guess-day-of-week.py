m1,d1,m2,d2=map(int,input().split())
a,b,c,d=m1,d1,m2,d2

day_of_the_week=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
months=[0,31,28,31,30,31,30,31,31,30,31,30,31]

if (m1==m2 and d1>d2) or (m1>m2):
    m1,d1,m2,d2=m2,d2,m1,d1

pass_day=0
while True:
    if m1==m2 and d1==d2:
        break
    d1+=1
    pass_day+=1
    if d1>months[m1]:
        d1=1
        m1+=1

dow=1
for i in range(pass_day):
    if (a==c and b>d) or a>c:
        dow=(dow-1)%7
    else:
        dow=(dow+1)%7
print(day_of_the_week[dow])