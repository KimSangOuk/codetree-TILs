n=int(input())
working=[0]*101
workers=[]
for i in range(n):
    s,e=map(int,input().split())
    workers.append((s,e))
    for j in range(s,e):
        working[j]+=1

answer=0

for i in range(n):
    for k in range(workers[i][0],workers[i][1]):
        working[k]-=1
    time=0
    for t in range(101):
        if working[t]>0:
            time+=1
    for k in range(workers[i][0],workers[i][1]):
        working[k]+=1
    answer=max(time,answer)
print(answer)