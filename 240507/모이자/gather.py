n=int(input())
arr=list(map(int,input().split()))

answer=int(1e9)

for i in range(n):
    sum_value=0
    for j in range(n):
        sum_value+=abs(j-i)*arr[j]
    answer=min(sum_value,answer)

print(answer)