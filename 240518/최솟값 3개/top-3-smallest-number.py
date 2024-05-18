import heapq

n=int(input())
arr=list(map(int,input().split()))
q=[]
for i in range(n):
    heapq.heappush(q,arr[i])
    if i<2:
        print(-1)
    else:
        a=heapq.heappop(q)
        b=heapq.heappop(q)
        c=heapq.heappop(q)
        print(a*b*c)
        heapq.heappush(q,a)
        heapq.heappush(q,b)
        heapq.heappush(q,c)