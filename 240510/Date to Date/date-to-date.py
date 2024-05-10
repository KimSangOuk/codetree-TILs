months=[0,31,28,31,30,31,30,31,31,30,31,30,31]
m1,d1,m2,d2=map(int,input().split())
answer=1

while True:
    if m2==m1 and d2==d1:
        break
    
    answer+=1
    d1+=1

    if d1>months[m1]:
        m1+=1
        d1=1
print(answer)