n=int(input())
arr=list(map(int,input().split()))

value=arr[0]
answer=0
for i in range(1,n):
    answer=max(answer,arr[i]-value)
    if arr[i]-value<0:
        answer=0
        value=arr[i]
        
print(answer)