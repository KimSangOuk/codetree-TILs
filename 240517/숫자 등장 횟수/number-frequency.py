n,m=map(int,input().split())
arr=list(map(int,input().split()))
cnt=dict()
for i in range(n):
    if arr[i] not in cnt:
        cnt[arr[i]]=1
    else:
        cnt[arr[i]]+=1
from_answer=list(map(int,input().split()))
for i in from_answer:
    if i in cnt:
        print(cnt[i],end=' ')
    else:
        print(0,end=' ')