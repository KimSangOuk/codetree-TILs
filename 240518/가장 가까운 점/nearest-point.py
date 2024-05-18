import heapq

n,m=map(int,input().split())
q=[]
for i in range(n):
    x,y=map(int,input().split())
    heapq.heappush(q,(abs(x)+abs(y),x,y))
for i in range(m):
    sum_value,x,y=heapq.heappop(q)
    heapq.heappush(q,(abs(x+2)+abs(y+2),x+2,y+2))

print(*q[0][1:])