import heapq

n=int(input())
arr=list(map(int,input().split()))
q=[]
for i in range(n):
    heapq.heappush(q,-arr[i])
while len(q)>=2:
    a=-heapq.heappop(q)
    b=-heapq.heappop(q)
    if a==b:
        continue
    heapq.heappush(q,-(a-b))
if len(q)==0:
    print(-1)
else:
    print(-q[0])