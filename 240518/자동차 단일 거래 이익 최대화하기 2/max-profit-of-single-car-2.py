n=int(input())
arr=list(map(int,input().split()))

value=arr[0]
answer=0
for i in range(1,n):
    if arr[i]-value<answer:
        answer=0
        value=arr[i]
    else:
        answer=max(answer,arr[i]-value)
print(answer)