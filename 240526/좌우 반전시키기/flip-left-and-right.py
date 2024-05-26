n=int(input())
arr=list(map(int,input().split()))
cnt=0
for i in range(1,n):
    if arr[i-1]==0:
        cnt+=1
        arr[i-1]=int(not bool(arr[i-1]))
        arr[i]=int(not bool(arr[i]))
        if i+1<n:
            arr[i+1]=int(not bool(arr[i]))
print(cnt)