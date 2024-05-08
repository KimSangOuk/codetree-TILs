n,k=map(int,input().split())
arr=[0]*101

for i in range(n):
    candy,basket=map(int,input().split())
    arr[basket]=candy

answer=0
if 101-2*k>0:
    for i in range(101-2*k):
        answer=max(answer,sum(arr[i:i+2*k+1]))
else:
    answer=sum(arr)

print(answer)