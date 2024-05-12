n,t=map(int,input().split())
arr=list(map(int,input().split()))

cnt=0
answer=0
for i in range(n):
    if i==0 or (arr[i-1]<=t and arr[i]>t) or arr[i]<=t:
        cnt=1
    else:
        cnt+=1
        answer=max(answer,cnt)
print(answer)