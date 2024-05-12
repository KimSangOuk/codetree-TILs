n=int(input())
arr=list(map(int,input().split()))
arr.sort()
answer=0
for i in range(n):
    a=arr[i]+arr[n*2-i-1]
    answer=max(answer,a)
print(answer)