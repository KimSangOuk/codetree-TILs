import heapq
n=int(input())
arr=list(map(int,input().split()))

answer=0
for i in range(1,n-1):
    tmp=arr[i:]
    heapq.heapify(tmp)
    heapq.heappop(tmp) 
    answer=max(sum(tmp)/len(tmp),answer)
print("{:.2f}".format(answer))