n=int(input())
height=[]
for i in range(n):
    height.append(int(input()))

answer=0
for i in range(0,max(height)):
    state=0
    cnt=0
    for j in range(n):
        if height[j]-i>0 and state==0:
            cnt+=1
            state=1
        elif height[j]-i<=0 and state==1:
            state=0
    answer=max(answer,cnt)
print(answer)