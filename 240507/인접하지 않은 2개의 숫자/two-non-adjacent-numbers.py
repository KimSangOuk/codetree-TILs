n=int(input())
arr=list(map(int,input().split()))
answer=0
for i in range(0,n-2):
    for j in range(i+2,n):
        answer=max(arr[i]+arr[j],answer)

print(answer)