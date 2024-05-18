n=int(input())
answer=0

cnt5=n//5
cnt2=0
answer=0
while True:
    if cnt5<0:
        answer=-1
    if (n-cnt5*5)==0:
        break
    elif (n-cnt5*5)%2==0:
        cnt2=(n-cnt5*5)//2
        break
    elif (n-cnt5*5)%2!=0:
        cnt5-=1
if answer==-1:
    print(answer)
else:
    print(cnt5+cnt2)