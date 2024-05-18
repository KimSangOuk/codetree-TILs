import heapq

n=int(input())
q=[]
for i in range(n):
    order=list(map(str,input().split()))
    if order[0]=='push':
        heapq.heappush(q,int(order[1]))
    elif order[0]=='size':
        print(len(q))
    elif order[0]=='empty':
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif order[0]=='pop':
        print(heapq.heappop(q))