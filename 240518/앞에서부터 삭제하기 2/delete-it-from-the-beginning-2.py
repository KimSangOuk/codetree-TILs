import heapq
n=int(input())
arr=list(map(int,input().split()))

answer=0
for i in range(1,n-1):
    tmp=arr[i:]
    q=[]
    for k in tmp:
       heapq.heappush(q,k)
    heapq.heappop(q) 
    answer=max(sum(q)/len(q),answer)
print("{:.2f}".format(answer))