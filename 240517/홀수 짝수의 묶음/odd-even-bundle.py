n=int(input())
arr=list(map(int,input().split()))
hol=0
jak=0
for i in range(n):
    if arr[i]%2==0:
        jak+=1
    else:
        hol+=1

answer=0
turn=0
while True:
    if turn==0:
        if jak>=1:
            jak-=1
            answer+=1
            turn=1
            # print(jak,hol,"짝하나")
            continue
        elif hol>=2:
            hol-=2
            answer+=1
            turn=1
            # print(jak,hol,"홀두개")
            continue
        else:
            break
    elif turn==1:
        if hol>=1:
            answer+=1
            hol-=1
            turn=0
            # print(jak,hol,"홀하나")
            continue
        else:
            break
if hol>0 or jak>0:
    answer-=1
print(answer)