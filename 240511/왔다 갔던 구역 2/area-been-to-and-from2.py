n=int(input())
arr=[0]*2001
start=1000
for i in range(n):
    dist,dir=input().split()
    dist=int(dist)
    if dir=='R':
        for j in range(dist):
            arr[start]+=1
            start+=1
    elif dir=='L':
        for j in range(dist):
            start-=1
            arr[start]+=1

answer=0
for i in range(2001):
    if arr[i]>1:
        answer+=1
print(answer)