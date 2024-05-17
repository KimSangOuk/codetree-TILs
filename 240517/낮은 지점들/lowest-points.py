pos=dict()
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    if x in pos:
        pos[x]=min(y,pos[x])
    else:
        pos[x]=y
answer=0
for i in pos.keys():
    answer+=pos[i]
print(answer)