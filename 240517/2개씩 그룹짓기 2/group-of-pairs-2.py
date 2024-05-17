n=int(input())
arr=list(map(int,input().split()))
arr.sort()
answer=int(1e9)
for i in range(n):
    answer=min(answer,abs(arr[i]-arr[i+n]))
print(answer)