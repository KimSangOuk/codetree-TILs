n,s=map(int,input().split())
arr=list(map(int,input().split()))

answer=int(1e9)
for i in range(n-1):
    for j in range(i+1,n):
        mid_sum=0
        for k in range(n):
            if k!=i and k!=j:
                mid_sum+=arr[k]
        answer=min(answer,abs(mid_sum-s))

print(answer)