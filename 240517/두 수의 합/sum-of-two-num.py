n,k=map(int,input().split())
cnt=dict()
arr=list(map(int,input().split()))
for i in range(n):
    if arr[i] not in cnt:
        cnt[arr[i]]=1
    else:
        cnt[arr[i]]+=1
answer=0
for i in list(set(cnt.keys())):
    if i==k-i:
        if i in cnt:
            answer+=(cnt[i])*(cnt[i]-1)
    else:
        if i in cnt and k-i in cnt:
            answer+=(cnt[i])*(cnt[k-i])
print(answer//2)