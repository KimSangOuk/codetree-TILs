import heapq

q=[]
n=int(input())
for i in range(n):
    k=int(input())
    if len(q)==0 and k==0:
        print(0)
    elif k!=0:
        heapq.heappush(q,k)
    elif k==0:
        print(heapq.heappop(q))