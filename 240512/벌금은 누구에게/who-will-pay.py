n,m,k=map(int,input().split())
arr=[0]*(n+1)

tf=False
for i in range(m):
    num=int(input())
    arr[num]+=1
    if arr[num]>=k:
        print(num)
        tf=True
if not tf:
    print(-1)