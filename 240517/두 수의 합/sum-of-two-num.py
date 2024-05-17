cnt=0
n,k=map(int,input().split())
diff=dict()
arr=list(map(int,input().split()))
for i in range(n):
    if k-arr[i] in diff:
        diff[k-arr[i]]=arr[i]
    else:
        diff[arr[i]]=0
for i in diff.keys():
    if diff[i]>0:
        cnt+=1
print(cnt)