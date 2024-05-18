import heapq
n=int(input())
arr=list(map(int,input().split()))

answer=0
min_value=int(1e9)
min_index=-1
sum_value=0
length=1
if arr[-1]>arr[-2]:
    min_index=n-2
    min_value=arr[-2]
    answer=arr[-1]
    sum_value=arr[-1]
else:
    min_index=n-1
    min_value=arr[-1]
    answer=arr[-2]
    sum_value=arr[-2]

for i in range(n-3,0,-1):
    if arr[i]<=min_value:
        sum_value+=min_value
        min_index=i
        min_value=arr[i]
    elif arr[i]>min_value:
        sum_value+=arr[i]
    length+=1
    answer=max(answer,sum_value/length)    
print("{:.2f}".format(answer))