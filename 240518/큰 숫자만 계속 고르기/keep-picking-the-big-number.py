import heapq

n,m=map(int,input().split())
q=[]
arr=list(map(int,input().split()))
for i in range(n):
    heapq.heappush(q,-arr[i])
for _ in range(m):
    k=-heapq.heappop(q)
    k-=1
    heapq.heappush(q,-k)
print(-q[0])