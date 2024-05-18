import heapq
n=int(input())
arr=list(map(int,input().split()))

answer=0
for i in range(n-2,0,-1):
    tmp=arr[i:]
    heapq.heapify(tmp)
    heapq.heappop(tmp)
    avg=sum(tmp)/len(tmp)
    if avg<answer:
        break
    else:
        answer=avg
print("{:.2f}".format(answer))