cnt=dict()
n,k=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(n):
    if arr[i] not in cnt:
        cnt[arr[i]]=1
    else:
        cnt[arr[i]]+=1
tmp=list()
for i in cnt.keys():
    tmp.append((i,cnt[i]))
tmp.sort(key=lambda x:(-x[1],-x[0]))
for i in range(k):
    print(tmp[i][0],end=' ')