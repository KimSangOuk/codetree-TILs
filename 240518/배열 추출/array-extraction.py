import heapq

q=[]
n=int(input())
for i in range(n):
    k=int(input())
    if k==0 and len(q)==0:
        print(0)
    elif k==0:
        print(-heapq.heappop(q))
    elif k!=0:
        heapq.heappush(q,-k)