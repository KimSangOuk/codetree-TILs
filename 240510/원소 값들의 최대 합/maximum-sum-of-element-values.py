n,m=map(int,input().split())
arr=list(map(int,input().split()))

answer=0
for i in range(n):
    start_index=i
    sum_value=0
    for j in range(m):
        sum_value+=arr[start_index]
        start_index=arr[start_index]-1
    answer=max(sum_value,answer)
print(answer)