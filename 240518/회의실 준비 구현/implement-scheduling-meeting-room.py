n=int(input())
classes=[]
for i in range(n):
    s,e=map(int,input().split())
    classes.append((s,e))
classes.sort(key=lambda x:x[1])
start,end=classes[0]
answer=1
for i in range(1,n):
    if end<=classes[i][0]:
        answer+=1
        start,end=classes[i]
print(answer)