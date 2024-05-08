n,h,t=map(int,input().split())
arr=list(map(int,input().split()))

answer=int(1e9)
for i in range(n-t+1):
    cost=0
    for j in range(i,i+t):
        cost+=abs(arr[j]-h)
    answer=min(cost,answer)
print(answer)