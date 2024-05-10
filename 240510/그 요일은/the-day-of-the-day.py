m1,d1,m2,d2=map(int,input().split())
a=input()
months=[31,29,31,30,31,30,31,31,30,31,30,31]

day_of_the_week=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

answer=0
pass_day=0
dow=0
while True:
    if m1==m2 and d1==d2:
        break
    d1+=1
    dow=(dow+1)%7
    if d1>months[m1]:
        d1=1
        m1+=1
    # if day_of_the_week[dow]==a:
    #     answer+=1
print(answer)