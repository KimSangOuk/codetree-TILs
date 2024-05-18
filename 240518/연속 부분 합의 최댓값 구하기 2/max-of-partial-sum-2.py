n=int(input())
arr=list(map(int,input().split()))
answer=-int(1e9)
sum_value=0
for i in range(n):
    sum_value+=arr[i]
    answer=max(sum_value,answer)
    if sum_value<0:
        sum_value=0
print(sum_value)