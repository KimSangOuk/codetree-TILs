n,t=map(int,input().split())
arr=list(map(int,input().split()))

cnt=0
answer=0
for i in range(n):
    if (arr[i-1]<=t and arr[i]>t) or (i==0 and arr[i]>t):
        cnt=1
    elif arr[i]<=t:
        cnt=0
    else:
        cnt+=1
    answer=max(answer,cnt)
print(answer)